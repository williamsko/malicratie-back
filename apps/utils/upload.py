def handle_uploaded_file(f,dest_path):
    with open(dest_path, 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)