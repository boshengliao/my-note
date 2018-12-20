下载  
=  

* 自己服务器下载  

        @app.route('/download/<filename>', methods=['GET'])
        def download(filename):
            def send_chunk(file_path, chunk_size=1024):
                with open(file_path, 'rb') as target_file:
                    continue_read = Ture
                    while continue_read:
                        chunk = target_file.read(chunk_size)
                        if not chunk:
                            continue_read = False
                            continue
                        yield chunk

            file_path = 'files/{}'.format(filename)
            return Response(send_chunk(file_path), content_type='application/octet-stream')

* 第三方下载

        file_url = "http://target_file.txt"

        r = requests.get(file_url, stream=True)

        filename = os.path.split(file_url)[1]
        with open(filename, "wb") as f:
            continue_write = True
            while continue_write:
                chunk = r.iter_content(chunk_size=1024)
                if not chunk:
                    continue_write = False
                    continue
                f.write(chunk)
