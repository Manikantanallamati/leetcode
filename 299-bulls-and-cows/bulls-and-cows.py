class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret = list(secret)
        guess = list(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
                secret[i] = '_'
                guess[i] ='_'
        # print(secret,guess)
        for i in range(len(secret)):
            if len(guess) == 0:
                break
            if secret[i] == '_':
                continue
            if secret[i] in guess:
                cows += 1
                guess.remove(secret[i])
            # print(secret,guess)
        return (str(bulls)+'A'+str(abs(cows))+'B')