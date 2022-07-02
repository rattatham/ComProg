def check(string):
  if len(string)<3:
    return string
  if '0'<=string[0]<='9' and '0'<=string[2]<='9':
    #print(string)
    if string[1]==".":
      #print(string,2)
      return string[0]+"void"+string[2] +check(string[3:])
  return string[0]+check(string[1:])

def checkfile(x):
  f=open(f"{x}","w")
  f.write("The history of Bangkok dates at least back to the early 15th century, when it was a village on the west bank of the Chao Phraya River, under the rule of Ayutthaya. Because of its strategic location near the mouth of the river, the town gradually increased in importance. Bangkok initially served as a customs outpost with forts on both sides of the river, and was the site of a siege in 1688 in which the French were expelled from Siam. After the fall of Ayutthaya to the Burmese Empire in 1767, the newly crowned King Taksin established his capital at the town, which became the base of the Thonburi Kingdom. In 1782, King Phutthayotfa Chulalok (Rama I) succeeded Taksin, moved the capital to the eastern bank's Rattanakosin Island, thus founding the Rattanakosin Kingdom. The City Pillar was erected on 21 April 1782, which is regarded as the date of foundation of the present city.Bangkok's economy gradually expanded through international trade, first with China, then with Western merchants returning in the early-to-mid 19th century. As the capital, Bangkok was the centre of Siam's modernization as it faced pressure from Western powers in the late-19th century. The reigns of Kings Mongkut (Rama IV, 1851–68) and Chulalongkorn (Rama V, 1868–1910) saw the introduction of the steam engine, printing press, rail transport and utilities infrastructure in the city, as well as formal education and healthcare. Bangkok became the centre stage for power struggles between the military and political elite as the country abolished absolute monarchy in 1932.Engraving of the city from British diplomat John Crawfurd's embassy in 1822.As Thailand allied with Japan in World War II, Bangkok was subjected to Allied bombing, but rapidly grew in the post-war period as a result of US aid and government-sponsored investment. Bangkok's role as a US military R&R destination boosted its tourism industry as well as firmly establishing it as a sex tourism destination. Disproportionate urban development led to increasing income inequalities and migration from rural areas into Bangkok; its population surged from 1.8 million to 3 million in the 1960s.Following the US withdrawal from Vietnam in 1973, Japanese businesses took over as leaders in investment, and the expansion of export-oriented manufacturing led to growth of the financial market in Bangkok. Rapid growth of the city continued through the 1980s and early 1990s, until it was stalled by the 1997 Asian financial crisis. By then, many public and social issues had emerged, among them the strain on infrastructure reflected in the city's notorious traffic jams. Bangkok's role as the nation's political stage continues to be seen in strings of popular protests, from the student uprisings in 1973 and 1976, anti-military demonstrations in 1992, and successive anti-government demonstrations by opposing groups from 2008 on.Administration of the city was first formalized by King Chulalongkorn in 1906, with the establishment of Monthon Krung Thep Phra Maha Nakhon as a national subdivision. In 1915, the monthon was split into several provinces, the administrative boundaries of which have since further changed. The city in its current form was created in 1972 with the formation of the Bangkok Metropolitan Administration (BMA), following the merger of Phra Nakhon Province on the eastern bank of the Chao Phraya and Thonburi Province on the west during the previous year.")
  f.close()
  f=open(f'{x}',"r")
  s=f.read()
  words=[words for words in s.split(" ")]
  f.close()
  return words


q=[]
p=[]

fname=input("File name: ")
words=checkfile(fname)

for i in range(len(words)):
  if "." in words[i]:
    q.append(words[i])
for i in q:
  x=check(i)
  p.append(x)

print(f"There are {len(p)-1} sentences and {len(words)} words.")
