import os
import sys
import gdown
import zipfile

'''
使用方法：
1. 下载单个数据集：python down.py <datasetname>
2. 下载所有数据集：python down.py -all
3. 查看所有数据集：python down.py -list
4. 查看帮助：python down.py -help
'''

file_links = {
    "TAXIBJ": "https://drive.google.com/file/d/1Ar-RixC_E4NaPNNP_ZUvKpIQePsBJ7zQ/view?usp=drive_link",
    "T_DRIVE20150206": "https://drive.google.com/file/d/1ZSUgMmkQGsBOIXkyR4665SsdMfRKvmcm/view?usp=drive_link",
    "T_DRIVE_SMALL": "https://drive.google.com/file/d/1JsclPvykCB3yUHTuUk3bCvIeojMTaJ5y/view?usp=drive_link",
    "SZ_TAXI": "https://drive.google.com/file/d/15JtkPjDx5KfvpZjUPA9PDu6EMeN_g7Fr/view?usp=drive_link",
    "SHMETRO": "https://drive.google.com/file/d/1sDHWx4Xi-nfnb5IRcRH2pKXIP0nVF-An/view?usp=drive_link",
    "serm_glove_word_vec": "https://drive.google.com/file/d/1hqi-WAqHHTsyoHRQ9WW-ynigYBfWYI2y/view?usp=drive_link",
    "Seattle": "https://drive.google.com/file/d/1MOyzSsw1qEyJhMzbTjWlPyvhs8SyoWRM/view?usp=drive_link",
    "ROTTERDAM": "https://drive.google.com/file/d/17aNUruX3rHwxr12RiT5LimajCVFt0Fp8/view?usp=drive_link",
    "Q-TRAFFIC": "https://drive.google.com/file/d/1t1DW82s1mw2yO76esvkiY0tA6H5aQZwv/view?usp=drive_link",
    "PORTO201307-201309": "https://drive.google.com/file/d/1dhMCLEB4B3ckGoqkjAmT9VfhC0lqQ-zj/view?usp=drive_link",
    "PEMSD8": "https://drive.google.com/file/d/1IYBfRTnhyrrpGofJNUzUDs6nc_I41SK-/view?usp=drive_link",
    "PEMSD7(M)": "https://drive.google.com/file/d/1i425AKg5DG807ldOaNzqKnBdChKC9zab/view?usp=drive_link",
    "PEMSD7": "https://drive.google.com/file/d/1GAmp0c0sOFuz8uIXp6Eu01soVjwhHvcz/view?usp=drive_link",
    "PEMSD4": "https://drive.google.com/file/d/1NuHSa1yY6ZPRsDdIv98zqmWDzAio3RAj/view?usp=drive_link",
    "PEMSD3": "https://drive.google.com/file/d/17zzexWxZTkfIoVM07RYoIZhFoM5qVgPJ/view?usp=drive_link",
    "PEMS_BAY": "https://drive.google.com/file/d/1M1MFTp58aiK8KHVkVjadgirbFO5A4Ht0/view?usp=drive_link",
    "NYCTaxi20160102": "https://drive.google.com/file/d/18QMWkrEdf2P-mkVe_clYrQecPWGbjS2J/view?usp=drive_link",
    "NYCTaxi20160103": "https://drive.google.com/file/d/1m_1uG5l6NIe3a_wNUwOC5eFd0_EtP8AM/view?usp=drive_link",
    "NYCTaxi20140112": "https://drive.google.com/file/d/1L9jNQbU5lDIpXHgk0evGlYeNOsKGzn5k/view?usp=drive_link",
    "NYCTAXI202004-202006_OD": "https://drive.google.com/file/d/1GdmfiakSgvh9TdzhtCPbCRDJIWtwsWIC/view?usp=drive_link",
    "NYCTAXI202001-202003_DYNA": "https://drive.google.com/file/d/10jMJ5RPDMEGi1qFw26IDem9dKKMo1g6n/view?usp=drive_link",
    "NYCTAXI201401-201403_GRID": "https://drive.google.com/file/d/1eDHTOIRCyQ6NARNpIB8SvquG5JpOkj8z/view?usp=drive_link",
    "NYCBike20160809": "https://drive.google.com/file/d/1aQ7-rsjlUIZgy3x6AhqWqX6R-Wl01RyL/view?usp=drive_link",
    "NYCBike20160708": "https://drive.google.com/file/d/1gTa0e8KHu-5ysCIgUK4zU_-gpJmcDxK2/view?usp=drive_link",
    "NYCBike20140409": "https://drive.google.com/file/d/1GRf5NyurxRG7a5RDjHliNvkFIS8nB7Lb/view?usp=drive_link",
    "NYCBike202007-202009": "https://drive.google.com/file/d/1Qz5xDm0cDjhWgbObj7mPI3UbB7wjf-eT/view?usp=drive_link",
    "NYC_TOD": "https://drive.google.com/file/d/1b_xTXGS-j-Cm6Ki8QfDxAdhznkH9Qq0p/view?usp=drive_link",
    "NYC_RISK": "https://drive.google.com/file/d/13E2oTSUs7JjFLt7bVHzR3rWJzmVSGKIZ/view?usp=drive_link",
    "Multi_Graph_Demand": "https://drive.google.com/file/d/12gZ1XlhU_-1kHufOy8pZtn3CFcIITlrr/view?usp=drive_link",
    "METR_LA": "https://drive.google.com/file/d/1ySgp1I8CdUDEcaJ4PE8m3409AwbIJoen/view?usp=drive_link",
    "M_DENSE": "https://drive.google.com/file/d/1kXHQF6pYLO-iCGMKW6AUkvgY6Vp09N8Z/view?usp=drive_link",
    "LOS_LOOP": "https://drive.google.com/file/d/1SAABiwtpFg7LE70C3jnxW8JckoRk6LoQ/view?usp=drive_link",
    "LOS_LOOP_SMALL": "https://drive.google.com/file/d/1zGWGzHL-hjFJdNPh6EDKjYY1uokmWVQW/view?usp=drive_link",
    "LOOP_SEATTLE": "https://drive.google.com/file/d/1C4zr2Jt4odCziRdKpRUDnxmSlTvn9v50/view?usp=drive_link",
    "instagram": "https://drive.google.com/file/d/1JEkPbQBbrQv8Twe-GzvWUaG7meiimGvT/view?usp=drive_link",
    "HZMETRO": "https://drive.google.com/file/d/1c51xHeaVQcSz2pzjf4GCr8pUHw3Va7jx/view?usp=drive_link",
    "gowalla": "https://drive.google.com/file/d/1c46BRdGEcM4fKiUMrB9zdmjI4uGE2oW6/view?usp=drive_link",
    "Global": "https://drive.google.com/file/d/1wLfGLamS7v9fvdj7uQRudx4Z6Uc3q2oo/view?usp=drive_link",
    "foursquare_tky": "https://drive.google.com/file/d/1-J36AE3DAwsydo8o3TqD41f5NnVd9AgL/view?usp=drive_link",
    "foursquare_nyc": "https://drive.google.com/file/d/1iyf48DIXC9IxI0FrWP8qz7aziWD-63Bx/view?usp=drive_link",
    "CHICAGO_RISK": "https://drive.google.com/file/d/1bQiqlZY07pIGEokxJT2yrxePqUKG77OG/view?usp=drive_link",
    "Chengdu_Taxi_Sample1": "https://drive.google.com/file/d/1P2faZ0lrwpGQ8RMkWYKLnH5OAvaaW3MJ/view?usp=drive_link",
    "brightkite": "https://drive.google.com/file/d/1B4lW_FDkTnTVO4UmYbgAY3qnbmFLCHmX/view?usp=drive_link",
    "bj_roadmap_node": "https://drive.google.com/file/d/1NsaEk-1O4k0pMTWaorodTbIUBRuPqMYf/view?usp=drive_link",
    "bj_roadmap_edge": "https://drive.google.com/file/d/1xihx2_x6MrhxPVbm7h545u1WS5dssqsV/view?usp=drive_link",
    "BIKEDC202007-202009": "https://drive.google.com/file/d/1ZfKDixfRjHzdKJEMDL4UkuXfwCJH_UWV/view?usp=drive_link",
    "BIKECHI202007-202009": "https://drive.google.com/file/d/1MtkDAb9wgBhTEyON7JBchvBtykC6GGib/view?usp=drive_link",
    "BIKECHI202007-202009-3600": "https://drive.google.com/file/d/1Ik1A5fH-GWqwh5A1a3NijvFw9JuB2IYu/view?usp=drive_link",
    "Beijing_Taxi_Sample": "https://drive.google.com/file/d/1LIiXetX7Q8vysVOlgBIwDEFA47y4vBxU/view?usp=drive_link",
    "BEIJING_SUBWAY_30MIN": "https://drive.google.com/file/d/1QHIeZb5vMIK7MY1d3ud02Bc4CgQrw3Kl/view?usp=drive_link",
    "BEIJING_SUBWAY_15MIN": "https://drive.google.com/file/d/1fegnbXO7Fblz3ppSBKMkDoYMoUmJDBC2/view?usp=drive_link",
    "BEIJING_SUBWAY_10MIN": "https://drive.google.com/file/d/1hunTsPUiC_rRdASOHs-PExhPsctvOlGn/view?usp=drive_link",
    "AUSTINRIDE20160701-20160930": "https://drive.google.com/file/d/1-GDS_2k5JHLSPWG95oXm01WoBqAaaiy8/view?usp=drive_link",
}



def download_google_drive(link, output_filename):
    file_id = link.split("/")[-2]
    download_url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(download_url, output_filename, quiet=False)

def unzip_file(zip_file, output_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

def download_and_unzip_all(file_links_dict):
    for filename, link in file_links_dict.items():
        output_filename = f"downloaded_file_{os.path.basename(filename)}.zip"
        output_folder = os.path.splitext(os.path.basename(filename))[0]
        download_google_drive(link, output_filename)
        unzip_file(output_filename, output_folder)
        print(f"File downloaded and unzipped successfully: {output_filename}")
        os.remove(output_filename)

if __name__ == "__main__":
    print("All file links:")
    for filename, link in file_links.items():
        print(f"{filename}: {link}")
    print()
    if len(sys.argv) == 2 and sys.argv[1] == "-all":
        download_and_unzip_all(file_links)
    elif len(sys.argv) == 2 and sys.argv[1] == "-help":
        print("Usage: python down.py <datasetname>")
        print("Usage: python down.py -all")
        sys.exit(1)
    elif len(sys.argv) == 2 and sys.argv[1] in file_links.keys():
        filename = sys.argv[1]
        download_and_unzip_all({filename: file_links[filename]})
        print(f"File downloaded and unzipped successfully to: {os.path.splitext(os.path.basename(filename))[0]}")
    elif len(sys.argv) == 2 and sys.argv[1] not in file_links.keys():
        print(f"Dataset {sys.argv[1]} not found!")
        sys.exit(1)
    elif len(sys.argv) == 2 and sys.argv[1] == "-list":
        print("All file links:")
        for filename, link in file_links.items():
            print(f"{filename}: {link}")
        sys.exit(1)
    else:
        print("Usage: python down.py <datasetname>")
        print("Usage: python down.py -all")
        sys.exit(1)