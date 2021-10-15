def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates 

def remove_duplicates(Text):
    ItemsNoDuplicates = [] # output variable
    for i in Text:
        if not i in ItemsNoDuplicates:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Text, Pattern)
    return Count

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 


Text ='GCTCCGTAGTCACCTAGTACTACAGAACTACAGAGCTCCGTACTTCATTAGCTCCGTAGTCACCTAGTGCTCCGTAGCGGTGTTAGCGGTGTTAACTACAGAGTCACCTAGTGCTCCGTACTTCATTAACTACAGAGTCACCTAGTCTTCATTAACTACAGACTTCATTAACTACAGAGTCACCTAGTGTCACCTAGTACTACAGACTTCATTAGCTCCGTACTTCATTAGCTCCGTAACTACAGAACTACAGACTTCATTAACTACAGAGCTCCGTAGTCACCTAGTGCGGTGTTACTTCATTAGTCACCTAGTGCTCCGTACTTCATTAACTACAGAGCTCCGTAGTCACCTAGTGTCACCTAGTGCTCCGTAGCGGTGTTAGCGGTGTTACTTCATTACTTCATTACTTCATTAGTCACCTAGTGCTCCGTAGTCACCTAGTACTACAGAGTCACCTAGTACTACAGAGTCACCTAGTGTCACCTAGTGCGGTGTTAGCGGTGTTAGCTCCGTAGCGGTGTTAACTACAGACTTCATTAACTACAGACTTCATTAGCTCCGTAGCGGTGTTAGTCACCTAGTGCGGTGTTAGTCACCTAGTGTCACCTAGTACTACAGAACTACAGAGTCACCTAGTACTACAGAGCTCCGTACTTCATTACTTCATTAGTCACCTAGTGTCACCTAGTGTCACCTAGTCTTCATTAGCTCCGTAGTCACCTAGTGTCACCTAGTACTACAGAACTACAGAGTCACCTAGTACTACAGAGTCACCTAGTACTACAGAGCTCCGTAGTCACCTAGTGTCACCTAGTGTCACCTAGTGCTCCGTAGCTCCGTACTTCATTAGCTCCGTACTTCATTAACTACAGAGCTCCGTAACTACAGACTTCATTAGTCACCTAGT'
k = 11

print (FrequentWords(Text, k))

