"""
Bu Program GNU/Linux dağıtımlarında çalışır
GNU Linux dağıtımı hakkında bilgi çıktısı veren bir programdır
Yiğit çıtak tarafından yapılmış ve geliştirilmektedir.

Lisans: GPL V3

Tanımlı dağıtımlar:
Arch Linux, Pardus, Ubuntu, Debian, Fedora, Kali Linux, Linux Mint,
Red Hat, Zorin Os, MX Linux, Pisi Linux, Turkman Linux, Open Suse,
Poppy Linux, Xubuntu

16 Adet Linux dağıtımı tanınmaktadır.
Daha fazlası çok yakında...
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
    system_info_shell = os.environ.get("SHELL")
    system_info_shell_name = system_info_shell[9::]

    system_control_distro_id = distro.id()



except:
    pass

version = 1.1


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

    ascii_redhat = colored("""
           .MMM..:MMMMMMM
          MMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMM.
         MMMMMMMMMMMMMMMMMMMMMM
        ,MMMMMMMMMMMMMMMMMMMMMM:
        MMMMMMMMMMMMMMMMMMMMMMMM
  .MMMM'  MMMMMMMMMMMMMMMMMMMMMM
 MMMMMM    `MMMMMMMMMMMMMMMMMMMM.
MMMMMMMM      MMMMMMMMMMMMMMMMMM .
MMMMMMMMM.       `MMMMMMMMMMMMM' MM.
MMMMMMMMMMM.                     MMMM
`MMMMMMMMMMMMM.                 ,MMMMM.
 `MMMMMMMMMMMMMMMMM.          ,MMMMMMMM.
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            `MMMMMMMMMMMMMMMMMMMMMMMM:
                ``MMMMMMMMMMMMMMMMM'
""","red")

    ascii_zorin = colored("""
        `osssssssssssssssssssso`
       .osssssssssssssssssssssso.
      .+oooooooooooooooooooooooo+.


  `::::::::::::::::::::::.         .:`
 `+ssssssssssssssssss+:.`     `.:+ssso`
.ossssssssssssssso/.       `-+ossssssso.
ssssssssssssso/-`      `-/osssssssssssss
.ossssssso/-`      .-/ossssssssssssssso.
 `+sss+:.      `.:+ssssssssssssssssss+`
  `:.         .::::::::::::::::::::::`


      .+oooooooooooooooooooooooo+.
       -osssssssssssssssssssssso-
        `osssssssssssssssssssso`
""","blue")

    ascii_turkman = colored("""
       @@@@@@@@@@%
  #@@@@@@@(       &(
 #@@@@@@
%@@@@@&
@@@@@@
&@@@@@#                            %@@@@@@@@#
 @@@@@@&                      @@@@@@@@%      (@%
  (@@@@@@@                   @@@@@@@
     #@@@@@@@@@@@@@@(       @@@@@@
                           @@@@@@
                           @@@@@@
     @@@@@@@@@&%@@          @@@@@@(
  %@@@@@@#         &(         &@@@@@@(
 @@@@@@(                        @@@@@@@@@%((#&@@
@@@@@@                              (%&@@&%(
@@@@@@
(@@@@@@
  @@@@@@%
    @@@@@@@&(     %&
       (@@@@@@@@@&
""","blue")

    ascii_opensuse = colored("""
           .;ldkO0000Okdl;.
       .;d00xl:^''''''^:ok00d;.
     .d00l'                'o00d.
   .d0Kd'  Okxol:;,.          :O0d.
  .OKKKK0kOKKKKKKKKKKOxo:,      lKO.
 ,0KKKKKKKKKKKKKKKK0P^,,,^dx:    ;00,
.OKKKKKKKKKKKKKKKKk'.oOPPb.'0k.   cKO.
:KKKKKKKKKKKKKKKKK: kKx..dd lKd   'OK:
dKKKKKKKKKKKOx0KKKd ^0KKKO' kKKc   dKd
dKKKKKKKKKKKK;.;oOKx,..^..;kKKK0.  dKd
:KKKKKKKKKKKK0o;...^cdxxOK0O/^^'  .0K:
 kKKKKKKKKKKKKKKK0x;,,......,;od  lKk
 '0KKKKKKKKKKKKKKKKKKKKK00KKOo^  c00'
  'kKKKOxddxkOO00000Okxoc;''   .dKk'
    l0Ko.                    .c00l'
     'l0Kk:.              .;xK0l'
        'lkK0xl:;,,,,;:ldO0kl'
            '^:ldxkkkkxdl:^'""","green")

    ascii_xubuntu = colored("""
           `.:/ossyyyysso/:.
        `.yyyyyyyyyyyyyyyyyyyy.`
      `yyyyyyyyyyyyyyyyyyyyyyyyyy`
    `yyyyyyyyyyyyyyyyyyyy::yyyyyyyy`
   .yyyyyyyyyyy/+:yyyyyyydsyyy+y}yyyy.
  yyyyyyy:o/yydMMM+yyyyy/M+y:hM+yyyyyy
 yyyyyyy+MMMyymMMMhyyyyyyM::mM+yyyyyyyy
`yyyyyyy+MMMMysMMMdyyyyydh:mN+yyyyyyyyy`
yyyyyyyy:NMMMMmMMMMmmdhyy+/y:yyyyyyyyyyy
yyyyyyyy+MMMMMMMMMMMMMMMMMMNho:yyyyyyyyy
yyyyyyyymMMMMMMMMMMMMMMMMMMMMMMyyyyyyyyy
yyyyyyy+MMMMMMMMMMMMMMMMMMMMMMMM/yyyyyyy
`yyyyyysMMMMMMMMMMMMMMMMMMMMMMmoyyyyyyy`
 yyyyyyoMMMMMMMMMMMMMMMMMMMmy+yyyyyyyyy
  yyyyy:mMMMMMMMMMMMMMMNho/yyyyyyyyyyy
   .yyyy:yNMMMMMMMNdyo:yyyyyyyyyyyyy.
    `yyyyyy:/++/::yyyyyyyyyyyyyyyyy`
      `yyyyyyyyyyyyyyyyyyyyyyyyyy`
        `.yyyyyyyyyyyyyyyyyyyy.`
           `.:/oosyyyysso/:.`""","blue")

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

ascii_pisi = """
    v//!-                      `:?lzC
   Q!::=zFx!  `;v6WBCicl;`  ,vCC!::#.
  ,%:::,'` +#%@@FQ@@.   ,cF%p``-',::a?
  +m:,'```3,/@@Q@@       "af- `-'"7f
  =o'.` /m'   :Q@:Qg         ,kl  `.|o
  :k` '+      'Narm           >d,  ii
   #`!p.        `C ,            'd+ %'
   !0m                           `6Kv
   =a                              m+
  !A     !L|:            :|L!      $:
 .8`     Q''%Q#'        '#Q%''Q     `0-
 :6      E|.6QQu        uQQ6.|E      p:
  i{      jts9?        ?9stj/      u
   |a`            -''.            `e>
    ,m+     '^ !`s@@@@a'"`+`     >e'
      !3|`|=>>r-  'U%:  '>>>=:`p!
       'xopE|      `'     `ledoz-
    `;=>>+``^llci/|==|/iclc;`'>>>>:
   `^`+~          ````          !!-^"""

ascii_poppy = """
           `-/osyyyysosyhhhhhyys+-
  -ohmNNmh+/hMMMMMMMMNNNNd+dMMMMNM+
 yMMMMNNmmddo/NMMMNNNNNNNNNo+NNNNNy
.NNNNNNmmmddds:MMNNNNNNNNNNNh:mNNN/
-NNNdyyyhdmmmd`dNNNNNmmmmNNmdd/os/
.Nm+shddyooo+/smNNNNmmmmNh.   :mmd.
 NNNNy:`   ./hmmmmmmmNNNN:     hNMh
 NMN-    -++- +NNNNNNNNNNm+..-sMMMM-
.MMo    oNNNNo hNNNNNNNNmhdNNNMMMMM+
.MMs    /NNNN/ dNmhs+:-`  yMMMMMMMM+
 mMM+     .. `sNN+.      hMMMMhhMMM-
 +MMMmo:...:sNMMMMMms:` hMMMMm.hMMy
  yMMMMMMMMMMMNdMMMMMM::/+o+//dMMd`
   sMMMMMMMMMMN+:oyyo:sMMMNNMMMNy`
    :mMMMMMMMMMMMmddNMMMMMMMMmh/
      /dMMMMMMMMMMMMMMMMMMNdy/`
        .+hNMMMMMMMMMNmdhs/.
            .:/+ooo+/:-."""

try:
    sys_info_show = f"""
==============================
Dağıtım           : {system_info_distro_name} {system_info_mimari} {system_info_distro_codename} {system_info_distro_V}
Çekirdek sürümü   : {system_info_kernel_name} {system_info_linux_kernel_version}
Bilgisayar adı    : {system_info_machine_name}
Kabuk             : {system_info_shell_name}
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
    print(system_info_version)

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

    elif system_control_distro_id == "pisi":
        print(ascii_pisi)

    elif system_control_distro_id == "rhel":
        print(ascii_redhat)

    elif system_control_distro_id == "zorin":
        print(ascii_zorin)

    elif system_control_distro_id == "turkman":
        print(ascii_turkman)

    elif system_control_distro_id == "opensuse-leap":
        print(ascii_opensuse)

    elif system_control_distro_id == "poppy":
        print(ascii_poppy)

    elif system_control_distro_id == "xubuntu":
        print(ascii_xubuntu)

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





