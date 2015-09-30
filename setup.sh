
re=".\w+"
echo "Linkando arquivos"

for entry in .*
do
	if [[ $entry =~ $re ]]; then
  		echo "ln -s ~/$entry $PWD/$entry" 
  	fi
done



# ln -s $HOME/dotfiles/.emacs.el $HOME/.emacs.el
# ln -s $HOME/dotfiles/.screenrc $HOME/.screenrc
# ln -s $HOME/dotfiles/.zshrc $HOME/.zshrc
# ln -s $HOME/dotfiles/.gitignore $HOME/.gitignore
# ln -s $HOME/dotfiles/.gdbinit $HOME/.gdbinit