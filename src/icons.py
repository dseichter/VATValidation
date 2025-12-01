# Copyright (c) 2024-2025 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import base64
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QByteArray


def get_icon_from_base64(data_str):
    """Convert base64 string to QIcon"""
    try:
        byte_array = QByteArray.fromBase64(data_str.encode('ascii'))
        pixmap = QPixmap()
        pixmap.loadFromData(byte_array)
        return QIcon(pixmap)
    except Exception as e:
        print(f"Error loading icon: {e}")
        return QIcon()


# Icon catalog - maps icon names to base64-encoded PNG data
ICON_DATA = {
    'playlist_add_check_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAx0lEQVRIS2NkoDFgpLH5DKMW'
    'EAxh+gYRZ53yf4JOQlLwvekuQQeiKKC5BaS4nli1BL1IrEG41NE3iIZEHIAc+Z3pPT9Dw7tP'
    'oGCjahzAQuA/w/8fP5rucWJYQCiIYOmeo1pRnoGZaeGPprsOsMjFZjjZFiAc8v/S96Z7+nDD'
    '/////qP5HhdyiiIviAplODl52b8hGwQMlm/AYOFGT67kWQAyBckSXIZTHskl4twcnNwvgcHC'
    'Q1RGozTXYtNPfhAR6ZpRCwgGFADzp1AZV9eQZwAAAABJRU5ErkJggg==',
    'overview_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABhUlEQVRIS2NkoDFgpLH5DPS1'
    'gLVawYKFmfk4Jb768/+vxe/mBydhZqD4gLNO+T8lhsP0fm+6Czd3mFuA7FV8QYcetEQHEc0t'
    'IDfCifYBzS0gNoiQHcJRr9T+o/FeJVH5gBwL0H1Ncj74z/D/6I+mezYgg9gq5bSYWFnPAw1h'
    'A/GBufTXv99/9X+1P7hBlA+wxQHMVxy1SssZGRkjsKn5/+//8h8t96JAcnh9gCuIWGsV9VkY'
    'mS7ADAf6qgFiGCOYBoG////r/Wq+d5ksCzhqlX8xMjKw4rPg/3+Gnz+a73KQFAcwH6HnXGw+'
    'AFkOUk8VC4DR++570z1hzjql98CAEkAuVcmygKNO+Scs5SBF8hugi0WBwfcJ6GxeYIr68aPp'
    'LieKBSy18pasjCzHcOVgYFAkAZPofPYaRXUmJiZ4UkSo//8B5oN//36p/Gx5jKgYSC0WOOqU'
    'lgBTTTTWZPr//5IfzfdiMZIpqZaw1iobszAynEHW9+fPH+PfbQ/PYc1opFpAjHoANaa7GSDw'
    'w54AAAAASUVORK5CYII=',
    'task_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABPUlEQVRIS2NkoDFgpLH5DBgW'
    'sFYrWLAwMx8nZPF/hv8NP5ruNRJSh2EBZ53yf0KaYPLEWEKWBSCDGRkYG0AWEbKELAu+N91l'
    '5KhTqifGErItALmeGEsosoAYSyi2AN0SUPAhJxKyLMCXyoaOBf8Y/vczMf3sY/jH8RjZR1Tx'
    'wb///yb9bL6fDw7/WqX5jIyMCTBLSLbgz++/FsysTFOAad4EbMj//9O+N9/LBjHZ65QmMDEw'
    'gi0iywJgMEz82XSvAKSZs1bpApA6Cje8VnEiEyNTHnqEk+yDf///Z/5svjcD2SBgsEwHBksG'
    'ttREsgUgQ/79+5vxs+XBTGiY4zQcJE+WBeCgZ/iXBqRMGRmYUodHPsDlC7KDCF+wkJRMWWrl'
    'LVkZWY4RayCyuj9//1r+bn1wAlmM/pU+OS7HpwcAySixGcSW7K8AAAAASUVORK5CYII=',
    'select_check_box_48dp_097e23_fill1_wght400_grad0_opsz48': 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAACAklEQVRoQ+2Zv06FMBTGTx0M'
    '10FNdHKE2YfQqA/goouJg+/gdK8EB+PkExgTF3XyAW6ML+F6cbm6aWI0ArkJtQwQ0ttCW/60'
    'GFih5fud75z2UBB0/EId1w89gG4HeweMdsAaOjcIwbFOkRjwdej5JzwN3BSyRs4tuXmkU3zy'
    'bgzwEnqTTWmAwcghY/VeZeITdVwH8gCBNzG22DsDQFJ6i6TSM50T5gO4sDiInSgRHkO8F3mv'
    '4zyE2QA58aloOp3NBWCJn4XrcPH2Yb4DguLNXIUkxJsHICneLAAF8eYAKIo3A0BAvDW0x+G5'
    'v8tqbNSXUXdjCdz336rdEt1zBRFehUv/K52XdMRPpCPe5rUz8gC5iAXf0RpcTT+VIAQjjxDa'
    'SeavDWAuYioQAuIT0SINZSUHsu1dBoIlfoE46c472QxAopolQgRCQnxzDqRhl4WQFN88gIwT'
    'CuLbARCBUBTfHkARxMr0J/0YyQqeU7Cspbi5ImYv/Ii8MC7aE+hNqmz/aBuAuTqpRD4d0z4A'
    'L50k0ibvih4ACiJQFN9uEXNqAk7t5XxjVpbz9H19Dsgq5TzfA2QriKajxd6Bf+NATTVZaRr5'
    'L7Iz+w4wOqz01toG48fA8/dZ0xWe+5Mj7XvywEFtOhQmIj85HsixOjeQxv64EGXtAUQj1dRz'
    'vQNNRVZ03s478Af5FdZAqrjQmwAAAABJRU5ErkJggg==',
    'output_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAA0ElEQVRIS2NkoDFgpLH5DPS1'
    'gLVawYKFmfk4Jb768/+vxe/mBydhZqD4gLNO+T8lhsP0fm+6CzcXqwXICkixEObAoWUBR61S'
    'OzCp/PjRdK8Rm28pC6IGZTHOfwwvQQb/Z/jfgM0SyiwAGsxWq6TLzMh4CZclFFsAMpi1St6I'
    'hYXlLDZLiLKA1OSLHFyDwwJCeYHiIMJnAW0jmR7JlLYZDS3sBk9ZRCjVEJLHWZqy1MpbsjKy'
    'HCNkAD75P3//Wv5ufXACa4VDicG49NK3TqaFDwCJx6QZ5nuPoQAAAABJRU5ErkJggg==',
    'exit_to_app_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAyUlEQVRIS2NkoDFgpLH5DPS1'
    'gLVawYKFmfk4Jb768/+vxe/mBydhZqD4gLNO+T8lhsP0fm+6CzcXqwXICkixEObAwWkByHWE'
    'fEa2DzhqlT8xMjLwgoILnyUELcAX3hx1yp+BEcaDzxKKLAAZTMgSghaQmkzRg2vgLSCU5ikO'
    'IppHMrYwBEcutZIpLgtAltA0oxGKG5g80amIUJGAy0KiLSDWxbjU4SxNWWrlLVkZWY5RYsGf'
    'v38tf7c+OIG1wqHEYFx66Vsn08IHAGsmmBkexiLBAAAAAElFTkSuQmCC',
    'globe_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAACQUlEQVRIS71Vy27TQBSdh53X'
    'AvZIbYwtNVVgAQKJErGAH0BCsAMWiK+AxFEUB3XJHyAkuo7Ehm1XPAXqAqEWShyC+IOqJMb2'
    'XGYQNn6MMwapeJX4Xp9z7rlz72B0xA8+YnykJNDt5lmK6RgjbCTFAEJuCMEN35ntLBNZSFDt'
    'nWwRQvbKVMgYrHkjd1+WKyWo2eYTjPEt8QEg+B6GcMV/MH0TAVR7KxYhlc+pigAeLxz3TpYk'
    'R1C1zTHB+JpIDMA/7ztf32U/qvct7lD+YQBjz3GvJyMpgspgtU2Z/kEkzA+8Bnr4bR4l611j'
    'Q6P0pcoyxti6N5p+jPJSBLEyH12ab06eJ8GKVMsI58NJjBv/0O3VcxrW3wKgg4UzOVbWFhlB'
    '0tqYgDd2jze25UPQCZxZzoq/qYCL3OUi24I8JogAkuUt81tFGOH8f4Ii1Xwepouha0ZxzW5e'
    '1LH2IpkfEv9UfAp/NzpXgeoYqizMWv2nyX1zmt03MjKxgxbDiSWL1QbGZczoNgDs86leSzVZ'
    '61odnaLU2S+qpqiKWt885CIbAYQbvvPldYpA/FGdjIhQRlDrcfWEbv/aArJBE4HK/ZXTVKu8'
    'V01nLj440aiz+qF4H7Kg/WM025WuCvGyaltPCUZXsyBFtui2cUHD9JXIVy67CJR7ucW9vJkk'
    'yRJo3WZHJ9ozPqrHRR5v7BZv7O2ssMILp3LPWKc6jUtddnyZDy1v0/0kyyl1ZXILHvGtciYD'
    'sBNAcPefr0zVwJWNKysoC1SU9xOO6O0ZJNmh+AAAAABJRU5ErkJggg==',
    'info_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABq0lEQVRIS92Vy07CQBSGZzq9'
    'wBu4EZEmQIgLDRvjQ5gY3enCxKfwUkJoE9/CxKhbEh/ChYmRhTGIpEV2vgEtLXMshE5oKb1A'
    '2Dirdvqf88259AxGa154zf5RLEBQtvYIJk2McH72MICQMQLnxFb7rahDLgRIN9sljuO+kkRI'
    'KRQtzeiGaUMBGaXwgDE+S+Lc0wCi92ajdx60mQNISqHJYXyUxrmnpQBNSzWOZ219ALGeqxAq'
    'fC7jnEEoLVtar+O9+wDZmuzWbvEa/Ori+Gt2Qx5G6ho688seBCVX5bHwFmnI6dIEQGUrSudw'
    'TtWu99/HGgbI1AodtxWLq6SHFRxQ21T1ig8Ql5604ME0TSyCJADPKI32HwHcIveC8yaY96Qp'
    'AoCuqRqThmEp4q/lA4GglyT9HVcDB0b7tvrz6gNM+jvuR5t2RlLdHEC82twhvPiRtiVn9SPq'
    'VIZavx06KsabkiI/cxgdLgOJHXaeU7fgj27BT9NAgMKTqRlzI37hhSNe5stEICzUKBi1oWTd'
    'Gt9hmkRXJo/JndtwuwEHLQeci6WvzDTpidLGRrAq6A/UNqkZQQBA9wAAAABJRU5ErkJggg==',
    'settings_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABy0lEQVRIS8WVsUoDQRCGZyPo'
    'niBaWFnJXWNaBUGsREVbCwvfQFFLQSF3JHcRFCyjoE9gYWEria2ggm1sbtHGTlAQb0PijRND'
    'TM7sJReSYJqQ7Ox+M/P/O8ugxx/W4/MhEkCzDFQl4tluy/0tA8oHdxeQHBuE5MtnfcaRAYq9'
    'DRVw05CMwQAi5uSjWOYT+i1jbEqtFT54eTHN4/oVAzaPCAXpuLw+NgDgCX2BxVi2E+HRx0WZ'
    'FrnqGQFAWCvaBdaL/wvQLP0EgG00OwzRP6N2FakV6/TdFx6Lx54ttsrrNYBpvNGvYdUm0uNc'
    'OmKtfo2beooglhKC8O457kgAULGjniHm5t9NYX7nlu6RuAFRfYRMwXG3lRqU/yQXJchFTjXA'
    'R7woOGJVlSlVYVEVqeoatc4kF6VDXfQDSBgmi4FdA8AlZbQSBQCIe54jDkIBXWrRESW009Ai'
    'rZsiA7ySbqNBF0WxKeAp2a7UyqYIeChtsatwkXpqduWiVQTufFQUv0qzpf3nm3CbWkaB2tBP'
    'ZV7LvFjS4sYdBU+GXMB7GogzNOyydB/m6NH4kLY71NSm0NG4HueQfJLNAYpUI78Hir3/8KK1'
    'a5kW8ZEq6IT5DV0UzhkLTBZwAAAAAElFTkSuQmCC',
    'restart_alt_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAB8ElEQVRIS+2Uvy8EURDH5z13'
    '9haFSkR19jRqEiQoLiR+1KLWEIWESiJus7nVUNCKwh+A6PyIRBQiCJ1CY++uEolKcXbduR2z'
    '61bWnf0hoZDY7r038/3Mm/m+ZfDLH/tlffgWIJqKdxXV3OV3igoNiMitg1HgR4h4YqiZZFhI'
    'KIAjbomWTHOssJTd+TFAZIEqj/CjSkEEODd4KQlKzvCDBd5AUOJD3Kw58BJBwDMjnen1OvcE'
    'xFLSHfW6zUoUFgnC3yElNMcLanZLkKVVDmzO2iPIM0Hqv4J8CSDxfcbYMGU+6qrW5IaQ2AmJ'
    'fQxZlBPULRtySvv9lZBqwCRExeZEwQrUb7UIbEPJSYoq8e6ikruoFHEgOtfrQbl/dp9XAaj6'
    'Pap+hOy4Ti2aDuMWISWtccZmKeeYcgZ8AR/VpLVAA7iFvPKqRP4BekVrq4csS6cMWC+iuWGo'
    '2akwQ47J0iblTCDCoaFqw75DBqWlTjTFvG3TtMZti/t9Y1Ajtide7fgHrRY2oOgPoFMxJV0D'
    'Yx1liLebXOJk0X2y6GjwQytH0LXzdO06a2kirryomXl3suN9+xUj5km8IfSvwgkUZekKgHU6'
    'a2eAjpXL+xe03+PVxeDHNNMmxBrNXet1fwIg3ugF6IPlzJPfiIIBYWzkE/P3AW90rtkZxCMZ'
    'TQAAAABJRU5ErkJggg==',
    'update_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAACFklEQVRIS8VVMU/bQBR+ZxLs'
    'Q4UJUQGFwVakDqhiSAc2JiqhrgwsVOofKAPKQhNZTpYIIfoPkNqRiaECAVK3Dq0Q6sRCHIa0'
    'aiWWDMSXVLnri1NHF2NfPBDFm+1773vf9973jsCQHzLk/DB6AMNeNIGnj7GSJZmtEOKCNdgm'
    '7P+6U6kQz2ADxoznlkcIpFUJEOieFd1JPCNowRKds55T6eWNBth9Nk/H9FqQWIB4yxz3UAbS'
    '8+a2RshB8M37y6Zp2vDZqAFs0Ci32t1A8dlz3NcqBrRgXgGQZfmMEsDImw1CCEXqZ0j9lRwY'
    'JUHnP4L8QJAXPTaxEu08naETT/6EaQaBYYDgPcwwlgFW8g0reSmAbzGn+ikc+AgAD6cgiUSJ'
    'xzRO4ziJkmyBvjEdBGAU0BcAhhDQZMWK8egAnYRG3mJoPj0KZKDRsMnfsclZIfgbVqx+jKuw'
    'BwLQYk5F90c1b+Vws5XRO5fonWwQ2+9k25qhHGLHVAZEuZrAeYmVqsWuF7oDwrVmpmnXbqIB'
    'OhIUrDqiTqHRTtBo60l0xpivGLOCCAwZUTkmchcF1eAOOscdtKYCQbm+YE9WfXNeV1JwBP/X'
    'TDcqetnZC3OUj/+UEufQnXsykP7efKdp5EPwzdPas2Df/g4Xo7xwgr2kYoAsG+zanQpXHtuD'
    'cDL/wmmnTnEBZuR/fo9asAllt64qYPRXZpIpGimDf0oE6hmtQBmAAAAAAElFTkSuQmCC',
    'select_check_box_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABFUlEQVRIS2NkoDFgpLH5DPS1'
    'gLVawYKFmfk4ub76/f+vw5/mBweR9aP4gLNO+T+5hv9n+O/yo+neXnT9WC343nSX7KADOvL1'
    'dyYGbYaGu69AllHVAqDhIENFQQbDHEk1C0AuB5orgmw41XzAWQt0OSOqy2FxQbEP8BmO1wfs'
    'NUqqjIyMZ3403+XDlbKAwfISKCeGEiy5KuwMk+/8JOgDWJL9/5/hMzZLcBnOKfj/B3IqxBtE'
    'uCzBajjQyTD1RFsA8ia6JfjCnCwLkC1BjgtsmZFsC9AtwZXTKbIAZgm+YoRiCwgVhIPHAkIu'
    'JSSPM5my1MpbsjKyHCNkAD75P3//Wv5ufXACa06mxGBcesmuWIh1DM0tAABdhMEZSH8tgAAA'
    'AABJRU5ErkJggg==',
    'save_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAA8klEQVRIS2NkoDFgpLH5DPS1'
    'gLVawYKFmfk4qb76z/C/4UfTvUZs+lB8wFmn/J9Uw2HqcVlCNQtAFmGzBKcF35vuEowfbD5G'
    't4TqFoB8guy4YWwBuamJ6CCiuwV/Gf6F/Wq6vxpkMVutQgQzI/NyXI4gKpKRNf/799/3Z8u9'
    'Lshi7DWKfkxMTBuxWUKyBbjyBK6cP/gs+Pfvn/vPlvu7UIKoTsmbiYERJdhg8iT7AKTx7/9/'
    '4b+a768CR3KdQjgzA/MKqkUyqUmWLB+QYglOC1hq5S1ZGVmOkWIYuto/f/9a/m59cAImTrBI'
    'psQykN6hbwEAh3OPGQEJf+AAAAAASUVORK5CYII=',
    'search_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABmElEQVRIS82TTUvDQBCGZ9La'
    'JnrwoAiK2Da5iwgqBa/+HOtV1ISSSE+CWG/+H7EKguI5rQVFi978yKYfWTfRFPqRbmobdG/J'
    'zswzs/O+CBEfjLg+/CFgLzUvxWM3ADjnT0mBPpMmXYFCpRZ28r4TiJp8hYBrQUUopefEKG+G'
    'gfQAJE2+ZF2vu8kOhR3bMIt+oaSq5ASEk5/vkqWbWR6kAyDl5SVwsOomWUJLgvw96SmQT4uS'
    'E7O8mGZzAQrVp0GQToCqvLK1zziOk7MPK6dBicmDzLYgCEVK4ZEY5mJ4gKZQrzPd5KpLChnb'
    'OUHIJLeJfwt4Yc3Ndqun+43baqL0zjLKy6F3IO6m05iIVUKr6M2ehOMHT1FBp58PrpkPVnk+'
    'YGZrMbPFh/KBHyyqcgkRN4KdDA1EmGCSqxPdTA41QRuyn0mhgLeAOO3/YwUvyOf7FhzVPkRN'
    'sdn4CR6Eq/dB3bUhFGxmOLFf7EgAtyAPMjKABxkLwIOoSv178ZQQvSz5zzU2gA8hNXMKzqAR'
    'CSCSJf/KaLykYe6/ACzguRkUcu9WAAAAAElFTkSuQmCC',
    'contact_support_24dp_097e23_fill1_wght400_grad0_opsz24': 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAACBElEQVRIS7VVTUvcURS970VN'
    'dCe4UfBjRqRLt1bcCf6CQou6EYWuWiiiWHDiNBEtKtiC29lUUEH8AYJbBbddCpPJotCCm1IX'
    'eaOTXG8sU2aS9+ZFi1nmnXvOveeelzB45oc9Mz9oBczV/AfGYJsxZtSbQUABiG+FW/mma1Ap'
    '0FEYemMw41BHEPJo9LZY+a7CSQVMe3iHAyzqyP9NhLgmXM+R4VMClj0wyaD9LCt5HVfDcOzO'
    '9S+TdSmBTnsYU+SIPwPX66u/twr5M9rJZBIXOOUUX9MLczW3xDnfkhYW+3qssPMYjHBOFH1f'
    '1ghG0YJYr5Qa65sEqLOIOkt1QakpMWDz9cK4U8KeEnSqkYxGvxVO2VQKSO1JjhNFy8F6ZVuF'
    'TdrU1K1OIELYq7rld2Yh95Uz/l4WhP8S+GtNbpYxvq9KWUsB1Q4S3tcab7UuSc0psilFkE5R'
    '1jtBYTgUjjetXHJ8oNpDhHhSdb1Xlp0/p0SNS/2/qXbB7o+gpUCHPfTaAOMoSYCI5/Q5mCCB'
    'KxIYSZ0D1Cii7dqbHANoF5vk80pWa2Jc8Cfshi/+70wCD1YVBl8Ca7vIIkLTHdB0MzKs/n9g'
    '0/8AYINsseRi+CtwvF5VI1qBZGFjCCg1V5SaF62mfLIAMvwsPnkfdRY+ReA64GE/FH2hI4/P'
    'Hy2QhbTlPXgsgQ5/Dz9Dvxn1eJMlAAAAAElFTkSuQmCC',
}


def get_icon(name):
    """Get QIcon by name from the catalog"""
    if name in ICON_DATA:
        return get_icon_from_base64(ICON_DATA[name])
    print(f"Warning: Icon '{name}' not found in catalog")
    return QIcon()