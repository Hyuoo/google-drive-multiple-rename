from drive import Drive


# for i in range(7):
#     files, page_token = get_files(service=service, page_token=page_token)
#     for file in files:
#         fid = file["id"]
#         fname = file["name"]
#         if re.match(r"[\d]+주차", (tmp:=fname.split("_"))[2]):
#             new_name = "_".join(tmp[:2] + tmp[3:])
#             try:
#                 input(new_name+" -??")
#                 rename_file(service, fid, new_name)
#                 print("OK")
#             except Exception as e:
#                 print(traceback.format_exc())
#                 exit(0)

import re

drive = Drive()
files = drive.get_file_list(file_type="text", startswith="is_empty", page_size=20, repeat=1)

for f in files:
    fid = f["id"]
    fname = f["name"]
    name, ext = fname.split(".")
    new_name = "changed_"+name+"p."+ext
    print(f"{name} >> {new_name}")
    drive.rename(fid, new_name)
    

# for file in files:
#     file_id = file["id"]
#     file_name = file["name"]
#     if re.match(r"[\d]+주차", (tmp:=file_name.split("_"))[2]):
#         new_name = "_".join(tmp[:2] + tmp[3:])
#         print(f"matched : {file_name}\n\t>>> {new_name}")
