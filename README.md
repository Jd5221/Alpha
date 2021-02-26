You want to save file "numbers" in your home directory. I have file=$HOME/./numbers this way the script can find it.
If you do move numbers just make sure you update the variable so it pulls from the right file path.

for those that arent to familiar with bash follow these tips
make sure you:
chmod +x def       #this makes the command executable
chmod +x numbers    #this makes the command executable

to find home directory do:
echo $HOME

as well you can make life easy and move def into your /bin folder

its a simple tool you can change what ever you want in it to make your life easy. 

I set the color variables, I only used red, but you can add them anywhere you want color.

But this is just a fun little script I made to practice my bash, and save some nano seconds when doing ctf's. 

