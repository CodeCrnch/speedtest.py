import speedtest


speed = speedtest.Speedtest()

ping = speed.get_best_server()['latency']
download_speed = speed.download()
upload_speed = speed.upload()

ping_ms = round(ping, 2)
download_speed_mbps = round(download_speed / 1048576, 2)
upload_speed_mbps = round(upload_speed / 1048576, 2)

print(f'Your ping is {ping_ms} ms')
print(f'Your download speed is {download_speed_mbps} MB/s')
print(f'Your upload speed is {upload_speed_mbps} MB/s')
