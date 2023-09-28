"""
Persistence -> Disk -> File Systems -> File: Abstraction
Data -> Memory -> File Organization
                  i) Text I/O: HRF, CSV,JSON,XML,YAML,...
                     x: int = 3615 -> Memory (4B)
                     Disk: 3|6|1|5 -> Disk (4B)
                     x: int = 1361578 -> Memory (4B)
                     Disk: 1|3|6|1|5|7|8 -> Disk (7B)
                     x: int = 42 -> Memory (4B)
                     Disk: 4|2 -> Disk (2B)

                 ii) Binary I/O: efficient JPG, PNG, MP4, MP3. ...
                     x: int = 3615 -> Memory (4B)
                                      Disk (4B)
                     x: int = 1361578 -> Memory (4B)
                                         Disk (4B)
                     x: int = 42 -> Memory (4B)
                                      Disk (4B)
"""