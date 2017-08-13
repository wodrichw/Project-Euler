n = 100;
ntri = 0;
npythag = 0;



for i in range(0, n+1):
    npythag += i*i;
    ntri += i;

diff = ntri*ntri - npythag;

print diff;
