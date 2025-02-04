#Clean


cleanAll() {
echo "Clean All"
rm -f *.exe
rm -f *.csv
}

usage() {
    echo "Launch build.sh with following parameters:
        - clean : remove all generated files
        - price : build the programme to price the products
        - hedge : build the programme to show delta hedging and gamma delta hedging
        - all   : build price & hedge
        "
}

build1() {
#Build le premier programme
echo "Build Price program"
g++ -Isrc/include src/Price.cpp src/lib/*.cpp -o Price.exe
}

build2() {
#Build le deuxieme programme
echo "Build Hedge program"
g++ -Isrc/include src/Hedge.cpp src/lib/*.cpp -o Hedge.exe
}

# Pas de parametres, on affiche l aide
if [[ ${#} -eq 0 ]]; then
    usage
    exit 1
fi

case $1 in
    clean)
        cleanAll
        exit 0
        ;;
    price)
        cleanAll
        build1
        exit 0
        ;;
    hedge)
        cleanAll
        build2
        exit 0
        ;;
    all)
        cleanAll
        build1
        build2
        exit 0
        ;;
    
esac