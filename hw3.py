class pet():

    def __init__(self, name, life, hungry):
        self.name = name
        self.life = life
        self.hungry = hungry

    def sleep(self):
        self.life+=1

    def feed(self):
        if self.hungry <= 0:
            print("我吃不下了")
        else:
            self.hungry -= 1

    def bad(self):
        self.life-=1

    def play(self):
        print("開開心心")
        self.life -= 1
        self.hungry += 1

    def state(self):
        if self.life <2 :
            print("我有點不舒服")
        
        print(self.name+" life:", self.life)
        print(self.name+" hungry:",self.hungry)

Name=input("name:")
Life=int(input("life:"))
Hungry=int(input("hungry:"))

K=pet(Name,Life,Hungry)


while True:

    comm=input("comm:")

    if comm=="sleep":
        K.sleep()
    elif  comm=="feed":
        K.feed()
    elif comm == "play":
        K.play()
    elif comm == "bad":
        K.bad()
    K.state()
