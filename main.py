"""
Bu Program GNU/Linux dağıtımlarında çalışır
GNU Linux dağıtımı hakkında bilgi çıktısı veren bir programdır
Yiğit çıtak tarafından yapılmış ve geliştirilmektedir.

Lisans: GPL V3
"""

try:
    import psutil
except:
    print("Hata: pstil nodülü yüklü değil ---> pip install pstil")
try:
    import sys
except:
    print("Hata: sys nodülü yüklü değil ---> pip install sys")
try:
    import distro
except:
    print("Hata: distro nodülü yüklü değil ---> pip install distro")
try:
    import os
except:
    print("Hata: os nodülü yüklü değil ---> pip install os")
try:
    import socket
except:
    print("Hata: socket nodülü yüklü değil ---> pip install socket")
try:
    from termcolor import colored
except:
    print("Hata: termcolor nodülü yüklü değil ---> pip install termcolor && pip install colored")

try:
    system_info_distro_name = distro.name()
    system_info_linux_kernel_version = os.uname().release
    system_info_mimari = os.uname().machine
    system_info_version = os.uname().version
    system_info_machine_name = os.uname().nodename
    system_info_kernel_name = os.uname().sysname
    system_info_local_ip = socket.gethostbyname(socket.gethostname())
    system_info_user_name = os.getlogin()
    system_info_distro_codename = distro.codename()
    system_info_distro_V = distro.version()

    system_control_distro_id = distro.id()
except:
    pass

version = 1.0


try:
    ascii_arch = colored("""
                  sMN-
                 +MMMm`
                /MMMMMd`
               :NMMMMMMy
              -NMMMMMMMMs
             .NMMMMMMMMMM+
            .mMMMMMMMMMMMM+
            oNMMMMMMMMMMMMM+
          `+:-+NMMMMMMMMMMMM+
          .sNMNhNMMMMMMMMMMMM/
        `hho/sNMMMMMMMMMMMMMMM/
       `.`omMMmMMMMMMMMMMMMMMMM+
      .mMNdshMMMMd+::oNMMMMMMMMMo
     .mMMMMMMMMM+     `yMMMMMMMMMs
    .NMMMMMMMMM/        yMMMMMMMMMy
   -NMMMMMMMMMh         `mNMMMMMMMMd`
  /NMMMNds+:.`             `-/oymMMMm.
 +Mmy/.                          `:smN:
/+.""","blue")

    ascii_pardus = colored("""
 .smNdy+-    `.:/osyyso+:.`    -+ydmNs.
/Md- -/ymMdmNNdhso/::/oshdNNmdMmy/. :dM/
mN.     oMdyy- -y          `-dMo     .Nm
.mN+`  sMy hN+ -:             yMs  `+Nm.
 `yMMddMs.dy `+`               sMddMMy`
   +MMMo  .`  .                 oMMM+
   `NM/    `````.`    `.`````    +MN`
   yM+   `.-:yhomy    ymohy:-.`   +My
   yM:          yo    oy          :My
   +Ms         .N`    `N.      +h sM+
   `MN      -   -::::::-   : :o:+`NM`
    yM/    sh   -dMMMMd-   ho  +y+My
    .dNhsohMh-//: /mm/ ://-yMyoshNd`
      `-ommNMm+:/. oo ./:+mMNmmo:`
     `/o+.-somNh- :yy: -hNmos-.+o/`
    ./` .s/`s+sMdd+``+ddMs+s`/s. `/.
        : -y.  -hNmddmNy.  .y- :
         -+       `..`       +-""","yellow")

    ascii_ubuntu = colored("""
    ----(_)
 _/  ---  \\
(_) |   |
  \\  --- _/
     ---(_)""","yellow")

    ascii_debian = colored('''
       _,met$$$$$gg.
    ,g$$$$$$$$$$$$$$$P.
  ,g$$P"        """Y$$.".
 ,$$P'              `$$$.
',$$P       ,ggs.     `$$b:
`d$$'     ,$P"'   $.$ $$$
 $$P      d$'     $,$$$P
 $$:      $$.   $-$,d$$'
 $$;      Y$b._   _,d$P'
 Y$$.    $`.$`"Y$$$$P"'
 $`$$b      $"-.__
  $`Y$$
   `Y$$.
     `$$b.
       `Y$$b.
          `"Y$b._
              `"""''','red')

    ascii_fedora = colored("""
       ,'''''.
       |   ,.  |
       |  |  '_'
  ,....|  |..
.'  ,_;|   ..'
|  |   |  |
|  ',_,'  |
 '.     ,'
   ''''' ""","blue")

    ascii_kali = colored("""
..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc',.
 .                   OMo           ':$dd$o.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd
                     ;XO,
                       ,d0Odlc;,..
                           ..',;:cdOOd::,.
                                    .:d;.':;.
                                       'd,  .'
                                         ;l   ..
                                          .o
                                            c
                                            .'
                                             .""","blue")

    ascii_mint = colored("""
 ___________
|_          \\
  | | _____ |
  | | | | | |
  | | | | | |
  | \\_____/ |
  \\_________/""","green")

    ascii_windows = colored("""
                                ..,
                    ....,,:;+ccllll
      ...,,+:;  cllllllllllllllllll
,cclllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll

llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
`'ccllllllllll  lllllllllllllllllll
       `' \\*::  :ccllllllllllllllll
                       ````''*::cll""","blue")

except:
    pass

ascii_mxlinux = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMM
MMMMMMMMMMNs..yMMMMMMMMMMMMMm: +NMMMMMMM
MMMMMMMMMN+    :mMMMMMMMMMNo` -dMMMMMMMM
MMMMMMMMMMMs.   `oNMMMMMMh- `sNMMMMMMMMM
MMMMMMMMMMMMN/    -hMMMN+  :dMMMMMMMMMMM
MMMMMMMMMMMMMMh-    +ms. .sMMMMMMMMMMMMM
MMMMMMMMMMMMMMMN+`   `  +NMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNMMd:    .dMMMMMMMMMMMMMMM
MMMMMMMMMMMMm/-hMd-     `sNMMMMMMMMMMMMM
MMMMMMMMMMNo`   -` :h/    -dMMMMMMMMMMMM
MMMMMMMMMd:       /NMMh-   `+NMMMMMMMMMM
MMMMMMMNo`         :mMMN+`   `-hMMMMMMMM
MMMMMMh.            `oNMMd:    `/mMMMMMM
MMMMm/                -hMd-      `sNMMMM
MMNs`                   -          :dMMM
Mm:                                 `oMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""

ascii_linux = """
                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'`"""


try:
    sys_info_show = f"""
{system_info_version}
Dağıtım           : {system_info_distro_name} {system_info_mimari} {system_info_distro_codename} {system_info_distro_V}
Çekirdek sürümü   : {system_info_kernel_name} {system_info_linux_kernel_version}
Bilgisayar adı    : {system_info_machine_name}
Yerel ip adresi   : {system_info_local_ip}
Kullanıcı adı     : {system_info_user_name}"""
except:
    pass


# CPU ve Bellek kullanım bilgisi
def guc_tuketim_bilgisi():
    while True:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent

            sys.stdout.write(f'\r[CPU : {cpu_usage}% | Bellek : {memory_usage}] ')
            sys.stdout.flush()

        except:
            print("")
            sys.exit()

def main():
    if system_control_distro_id== "arch":
        print(ascii_arch)

    elif system_control_distro_id == "pardus":
        print(ascii_pardus)

    elif system_control_distro_id == "ubuntu":
        print(ascii_ubuntu)

    elif system_control_distro_id == "debian":
        print(ascii_debian)

    elif system_control_distro_id == "fedora":
        print(ascii_fedora)

    elif system_control_distro_id == "kali":
        print(ascii_kali)

    elif system_control_distro_id == "linuxmint":
        print(ascii_mint)

    elif system_control_distro_id == "mx":
        print(ascii_mxlinux)

    else:
        print(ascii_linux)

    print(sys_info_show)
    print("==============================")
    guc_tuketim_bilgisi()


def notLinux():
    print(ascii_windows)
    print("\nHata: işletim sisteminiz Linux değil :/")

if __name__ == "__main__":
    try:
        if system_info_kernel_name == "Linux":
            main()
        else:
            notLinux()
    except:
        pass





