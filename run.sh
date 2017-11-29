./extract.sh
g++ -o mst MST.cpp -O2 -std=c++11
g++ -o mst2graph MSTResult2graphTheoritic.cpp -O2 -std=c++11

python3 pre-cpp.py > dataset1

head -n 1 dataset1 > dataset2
echo 2 >> dataset2

./mst < dataset1 >> dataset2
./mst2graph < dataset2 > dataset3


