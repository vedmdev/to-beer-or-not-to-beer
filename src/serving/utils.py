import os

def save_file_to_local_file_store(request, filekey=None):
    # print("files in the request->", request.files)
    if not request.files:
        print('No files found in the request')
        raise Exception(msg='No files found in the request')
    if filekey:
        file = request.files[filekey]
    else:
        file = list(request.files.values())[0]
    # print("file->", file)
    if file: # and self._is_allowed_file_ext(file.filename)
        # TODO: use secure_filename
        # from werkzeug.utils import secure_filename
        # filename = secure_filename(file.filename)
        filename = file.filename
        filelocation = os.path.join("data/received_files", filename)
        file.save(filelocation)
        # return Response('Upload successful'), 201
        return {"message":"Upload success", "filelocation":filelocation}
    else:
        raise Exception("File extention not allowed")