import cv2
import numpy as np
import requests

# 1. جلب صورة الخريطة أو الأقمار الصناعية باستخدام Google Static Maps API
def fetch_map_image(lat, lng, zoom=19, api_key="YOUR_API_KEY"):
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom={zoom}&size=600x600&maptype=satellite&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return img
    return None

# 2. البحث عن شكل الرادار داخل الصورة باستخدام OpenCV
def find_radar(map_img, template_img):
    map_gray = cv2.cvtColor(map_img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    
    # إجراء مطابقة القالب
    result = cv2.matchTemplate(map_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # نسبة التطابقة المقبولة (مثلاً 75% أو أعلى)
    threshold = 0.75
    if max_val >= threshold:
        h, w = template_gray.shape
        top_left = max_loc
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        return (center_x, center_y), max_val
    return None, max_val

# 3. تحويل إحداثيات البكسل إلى خطوط طول وعرض (GPS)
def pixel_to_latlng(pixel_x, pixel_y, center_lat, center_lng, zoom, img_size=600):
    # حساب المسافة التي يمثلها البكسل الواحد بالمتر بناءً على مستوى التكبير Zoom
    meters_per_pixel = (156543.03392 * np.cos(np.radians(center_lat))) / (2 ** zoom)
    
    # حساب الإزاحة عن مركز الصورة بالبكسل
    dx_pixels = pixel_x - (img_size / 2)
    dy_pixels = (img_size / 2) - pixel_y  # محور Y معكوس في مصفوفات الصور
    
    # تحويل الإزاحة إلى أمتار
    dx_meters = dx_pixels * meters_per_pixel
    dy_meters = dy_pixels * meters_per_pixel
    
    # تحويل الأمتار إلى درجات جغرافية تقريبية
    delta_lat = dy_meters / 111320.0
    delta_lng = dx_meters / (111320.0 * np.cos(np.radians(center_lat)))
    
    return center_lat + delta_lat, center_lng + delta_lng

# مثال عملي لتشغيل الدوال
if __name__ == "__main__":
    # إحداثيات مركز المنطقة المراد البحث فيها
    target_lat, target_lng = 30.0444, 31.2357
    zoom_level = 19
    
    # جلب صورة الخريطة
    map_image = fetch_map_image(target_lat, target_lng, zoom=zoom_level)
    
    if map_image is not None:
        # قراءة صورة نموذج الرادار القصي (Template) التي قمت بتجهيزها مسبقاً
        template_image = cv2.imread('radar_template.png')
        
        if template_image is not None:
            pixel_pos, confidence = find_radar(map_image, template_image)
            
            if pixel_pos:
                radar_lat, radar_lng = pixel_to_latlng(
                    pixel_pos[0], pixel_pos[1], target_lat, target_lng, zoom_level
                )
                print(f"تم العثور على الرادار بدقة مطابقة {confidence * 100:.2f}%")
                print(f"إحداثيات الرادار: خط الطول {radar_lng}, خط العرض {radar_lat}")
            else:
                print("لم يتم العثور على أي رادار مطابق في هذه المنطقة.")
