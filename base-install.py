#! /usr/bin/env python3

# Les imports 
import os 

# Les variables
yes = "yes"

def main():
    print("Félicitations, vous venez d'installer la version BASE de la distribution GNU/LINUX NuTyX !! ")
    print("Avant d'aller plus loin, veuillez svp lire le prérequi : Veuillez vérifier que votre ordinateur est connecté à internet")
    yes_or_no = input("Alors ? [yes ou no ] : ")
    if yes == yes_or_no :
        print("Nous installons la BASE d'une installation graphique ... ")
        os.system("sudo cards install lxdm xorg-xf86-video-intel zip unzip xdg-user-dirs sound-theme-freedesktop alsa-utils pavucontrol gvfs xorg-xf86-input-synaptics network-manager-applet")
        firefox_install = input("Souhaitez vous installer un navigateur web ? [yes or no ] : ")
        if firefox_install == yes:
            os.system("sudo cards install firefox")
        thunderbird_install = input("Souhaitez vous un client de messagerie ? : )
        if thunderbird_install == yes :
            os.system("sudo cards install thunderbird")
        print("Nous syncronisons les dépôts de votre os")
        os.system("sudo cards sync && sudo cards upgrade")
        install =input("Quels paquets souhaitez vous installer ? : ")
        os.system("sudo cards install " + install )
        flatpak =input("Souhaitez vous installer les flatpaks ? : ")
        if flatpak == yes :
            get_flatpak =input("Quels paquets flatpaks voulez vous installer ? : ")
            try :
                os.system("flatpak install " + get_flatpak )
            except :
                os.system("sudo cards install flatpak")
                os.system("flatpak install " + get_flatpak )
        
        if flatpak != yes : 
            print("Nous nettoyons les archives binaires")
            os.system("sudo cards purge")
            print("Done")
      
    if yes != yes_or_no :
        exit()
        
        
if __name__ == "__main__":
    main()
