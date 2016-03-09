#include <cstdio>
#include <fstream>
#include <vector>

using namespace std;

const int PAGE_NUM = 0x80;
const int PAGE_SIZE = 32;

int vAddress;
vector<int*> memory;
void read_table(){
	fstream fin("table.txt");
	int cnt = 0;
	while (fin.good()){
		string buf;
		fin >> buf;
		fin >> buf;
		int *tmp = new int[PAGE_SIZE];
		for (int i = 0; i < PAGE_SIZE; i++)
			fin >> hex >> tmp[i];
		memory.push_back(tmp);
		cnt++;
	}
	printf("cnt:%d\n", cnt);
}
int main()
{

    read_table();
    printf("Input Virtual Address:0x");
    scanf("%x", &vAddress);
    printf("Virtual Address %x:\n", vAddress);
    int index1 = (vAddress & 0x7c00) >> 10;
    int index2 = (vAddress & 0x03e0) >> 5;
    int offset = vAddress & 0x001f;

    int pde = memory[0x11][index1];
    int valid = (pde & 0x80)?1:0;
    printf("%x\n", pde);
    int pt = pde & 0x7f;
    printf("  --> pde index:0x%x  pde contents:(valid %d, pt 0x%x)\n", index1, valid, pt);
    if (!valid)
    {
        puts("    --> Fault (page directory entry not valid)");
        return 0;
    }
    else
    {
        int pte = memory[pt][index2];
        int pfn = pte & 0x7f;
        valid = (pte & 0x80)?1:0;
        printf("    --> pte index:0x%x  pte contents:(valid %d, pfn 0x%x)\n", index2, valid, pfn);

        if (!valid)
        {
            puts("      --> Fault (page directory entry not valid)\n");
            return 0;
        }
        else
        {
            int value = memory[pfn][offset];
            int pAddress = (pfn << 5) + offset;
            printf("      --> Translates to Physical Address 0x%x --> Value: %x", pAddress, value);
        }
    }
    return 0;
}
