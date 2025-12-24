import os
from modules.downup.downloader import downloader


def main():
    url = 'https://speed.hetzner.de/1MB.bin'
    d = downloader(threads=4)
    out_dir = 'tmp_test_downloads'
    os.makedirs(out_dir, exist_ok=True)
    ok = d.download(url, out_dir)
    path = os.path.join(out_dir, d.getname(url))
    assert ok, 'download() returned False'
    size_remote = d.getlenght(url)
    size_local = os.path.getsize(path)
    print('Remote:', size_remote, 'Local:', size_local)
    assert size_local == size_remote, f'size mismatch: {size_local} != {size_remote}'
    print('OK')


if __name__ == '__main__':
    main()
