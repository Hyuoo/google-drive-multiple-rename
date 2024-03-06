from drive import Drive


drive = Drive()

files = drive.get_file_list(
    file_type="text",
    startswith="Bam",
    page_size=20,
    repeat=1
    )

for f in files:
    file_id, file_name = f["id"], f["name"]
    new_name = "changed_" + file_name.replace(" ", "_")
    
    if (input(f"rename {file_name} >> {new_name}? (Enter Y/N) ")) not in ("N", "n"):
        # Y는 훼이크
        drive.rename(file_id, new_name)
        print("commit")
