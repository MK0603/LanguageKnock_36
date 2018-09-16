# coding: UTF-8
from LanguageKnock_30 import makeMecabPattern


class extractVersMethods:
    def checkNovel(self, novelListS):
        wordCounter={}
        for sentenseList in novelListS:
            for word in sentenseList:
                if word["surface"] in wordCounter.keys():
                    wordCounter[word["surface"]] = wordCounter[word["surface"]]+1
                else:
                    wordCounter.setdefault(word["surface"],1)
        sortedWordCounter=sorted(wordCounter.items(),key=lambda x:x[1],reverse=True)
        return sortedWordCounter


                

if __name__ == '__main__':
    cal = extractVersMethods()
    novelListS = makeMecabPattern()
    ans = cal.checkNovel(novelListS)
    print (ans)
