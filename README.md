You want to save file "Alpha" in your home directory. I have file=$HOME/Alpha/./numbers this way the script can find it.
If you do move numbers just make sure you update the variable so it pulls from the right file path.

for those that arent to familiar with bash follow these tips
make sure you:
chmod +x def       #this makes the command executable
chmod +x numbers    #this makes the command executable


!runme.sh!!!!!!!!!!!!!!!!!
I made a runme.sh file just to make life simple, it should check on some dependencies, mark the files as executable and copy the def file to usr/bin
all you have to do is 
chmod +x runme.sh
then
sudo ./runme.sh

to find home directory do:
echo $HOME

as well you can make life easy and move def into your /bin folder

its a simple tool you can change what ever you want in it to make your life easy. 

I set the color variables, I only used red, but you can add them anywhere you want color.

But this is just a fun little script I made to practice my bash, and save some nano seconds when doing ctf's. 

