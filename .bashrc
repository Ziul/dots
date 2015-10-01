
export WORKON_HOME=$HOME/.virtualenvs
export MSYS_HOME=C:\msys\1.0
export EDITOR=vim
source /usr/local/bin/virtualenvwrapper.sh

export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"

eval $(thefuck --alias)

PERL_MB_OPT="--install_base \"/home/luiz/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/luiz/perl5"; export PERL_MM_OPT;