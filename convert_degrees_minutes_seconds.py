import pandas as pd

# قراءة بيانات الإحداثيات من ملف Excel
data = pd.read_excel('D:/Work_Project/Work GIS/coor1.xlsx')

# استخراج القيم الأصلية للإحداثيات
data['Coordinates'] = data['Coordinates'].str.strip()  # إزالة الفراغات الزائدة
data['Latitude'] = data['Coordinates'].str.extract(r'(\d+°\s?\d+\'\s?\d+\.\d+")N') # تقسيم عمود الشماليات حسب الدرجات والدقايق و
data['Longitude'] = data['Coordinates'].str.extract(r'(\d+°\s?\d+\'\s?\d+\.\d+")E')# تقسيم عمود الشرقيات حسب الدرجات والدقايق 

# إضافة عمود للشماليات (Latitude)
data['Latitude_deg'] = data['Latitude'].str.extract(r'(\d+)°')
data['Latitude_min'] = data['Latitude'].str.extract(r"(\d+)'")
data['Latitude_sec'] = data['Latitude'].str.extract(r'(\d+\.\d+)"')
data['Latitude_dir'] = data['Latitude'].str.extract(r'([NS])')

# إضافة عمود للشرقيات (Longitude)
data['Longitude_deg'] = data['Longitude'].str.extract(r'(\d+)°', expand=False)
data['Longitude_min'] = data['Longitude'].str.extract(r"(\d+)'", expand=False)
data['Longitude_sec'] = data['Longitude'].str.extract(r'(\d+\.\d+)"', expand=False)
data['Longitude_dir'] = data['Longitude'].str.extract(r'([EW])', expand=False)

# function  ديه لو لقى النوع الاول من الاحدثيات الى هى عشرية وفيها (,) يتعامل معاها بفصلها
# تحويل الإحداثيات إلى الصيغة العشرية
def convert_to_decimal(coordinates):
    
    if ',' in coordinates:
        lat, lon = coordinates.split(',')
        return float(lat), float(lon)
    # else:
    #     return None, None

data[['Latitude_decimal', 'Longitude_decimal']] = data['Coordinates'].apply(convert_to_decimal).apply(pd.Series)

# تحديث القيم الأصلية للإحداثيات
data['Latitude'] = data['Latitude_decimal'].fillna(data['Latitude'])
data['Longitude'] = data['Longitude_decimal'].fillna(data['Longitude'])

# عرض النتيجة
print(data)

# حفظ البيانات في ملف Excel جديد
data.to_excel('D:/Work_Project/Work GIS/coor1.xlsx', index=False)


def split_coordinates(coordinates):
    parts = coordinates.split(' ')
    
    lat_part = parts[0] if len(parts) > 0 else ''
    lon_part = parts[1] if len(parts) > 1 else ''
    
    lat = None
    lon = None
    
    if lat_part and lon_part:
        lat_split = lat_part.split('"')
        lon_split = lon_part.split('"')
        
        if len(lat_split) > 1 and lat_split[0].replace('.', '').isdigit():
            lat = float(lat_split[0])
        
        if len(lon_split) > 1 and lon_split[0].replace('.', '').isdigit():
            lon = float(lon_split[0])
    
    return lat, lon





data[['Latitude second case', 'Longitude second case']] = data['Coordinates'].apply(split_coordinates).apply(pd.Series)


# # حفظ البيانات في ملف Excel جديد
data.to_excel('D:/Work_Project/Work GIS/coor1.xlsx', index=False)




def convert_to_decimal(degrees, minutes, seconds):
    if pd.notnull(degrees) and pd.notnull(minutes) and pd.notnull(seconds):
        degrees = int(degrees)
        minutes = int(minutes)
        seconds = float(seconds)
        decimal_value = degrees + (minutes / 60) + (seconds / 3600)
        return decimal_value
    
    # else:
    #     return None

data['Latitude_decimal'] = data.apply(lambda row: convert_to_decimal(row['Latitude_deg'], row['Latitude_min'], row['Latitude_sec']), axis=1)
data['Longitude_decimal'] = data.apply(lambda row: convert_to_decimal(row['Longitude_deg'], row['Longitude_min'], row['Longitude_sec']), axis=1)

# تحديث الإحداثيات العشرية إذا تم العثور عليها
data['Latitude_decimal'] = data['Latitude_decimal'].fillna(data['Latitude'].str.extract(r'(\d+\.\d+)', expand=False).astype(float))
data['Longitude_decimal'] = data['Longitude_decimal'].fillna(data['Longitude'].str.extract(r'(\d+\.\d+)', expand=False).astype(float))

# عرض النتيجة
print(data)

# حفظ البيانات في ملف Excel جديد
data.to_excel('D:/Work_Project/Work GIS/coor1.xlsx', index=False)



# # # import pandas as pd

# # قراءة بيانات الإحداثيات من ملف Excel
# data = pd.read_excel('D:/Work_Project/Work GIS/coor2.xlsx')

# استخراج القيم الأصلية للإحداثيات
# data['Coordinates'] = data['Coordinates'].str.strip()  # إزالة الفراغات الزائدة

# تحويل الإحداثيات إلى درجات عشرية إذا كانت بالصيغة "عدد,عدد"
# def convert_to_decimal(coordinates):
    
#     if ',' in coordinates:
#         lat, lon = coordinates.split(',')
#         return float(lat), float(lon)
#     # else:
#     #     return None, None

# data[['Latitude_decimal', 'Longitude_decimal']] = data['Coordinates'].apply(convert_to_decimal).apply(pd.Series)

# # تحديث القيم الأصلية للإحداثيات
# data['Latitude'] = data['Latitude_decimal'].fillna(data['Latitude'])
# data['Longitude'] = data['Longitude_decimal'].fillna(data['Longitude'])

# # عرض النتيجة
# print(data)

# # حفظ البيانات في ملف Excel جديد
# data.to_excel('D:/Work_Project/Work GIS/coor1.xlsx', index=False)
