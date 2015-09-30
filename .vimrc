set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'

Plugin 'flazz/vim-colorschemes'
Plugin 'bling/vim-airline'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/syntastic'
Plugin 'bitc/vim-bad-whitespace'
Plugin 'majutsushi/tagbar'
Plugin 'justinmk/vim-syntax-extra'
Plugin 'Valloric/YouCompleteMe'
Plugin 'nvie/vim-flake8'

call vundle#end()
filetype plugin indent on

syntax on
set laststatus=2


let g:airline_powerline_fonts = 1
set noshowmode

autocmd vimenter * if !argc() | NERDTree | endif
map <C-n> :NERDTreeToggle<CR>
nmap <F8> :TagbarToggle<CR>

set number

autocmd FileType python,sh setlocal expandtab shiftwidth=4 softtabstop=4
autocmd FileType html setlocal expandtab shiftwidth=2 softtabstop=2

set nowrap
set hlsearch
set visualbell
set title
set ttyfast
set cursorline
set diffopt=filler
set diffopt+=iwhite
set hidden
set history=1000

set formatoptions=
set formatoptions+=c
set formatoptions+=r
set formatoptions+=o
set formatoptions+=q
set formatoptions+=n
set formatoptions+=2
set formatoptions+=l

set mouse=a
set ttymouse=xterm2
