from discord.ext import commands
import secrets 
import requests
import bs4 





class TruthDare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def t(self, ctx):
        flag = secrets.choice([1,2,3])

        if flag == 1:
            truthlist = ["When was the last time you told a lie?", "What is your biggest fear?", "Who do you have a crush on?", "If you had to date someone in this room, who would it be?", "Have you ever been cheated on someone", "What was your first kiss like?", "Who is the last person that you stalked on social media?", "What is the craziest event that you have ever been to?", "What is the craziest event that you have ever been to?", "What is the worst dream that you have had?", "Why did your last relationship end?", "What is the most embarrassing thing that has happened to you this year?", "What is the most embarrassing thing that has happened to you this year?", "Who is your celebrity crush?", "What don’t you like about your boyfriend or girlfriend?", "Have you ever hooked up with the same sex?", "What is a secret that you have never told anyone before?", "How many people have you kissed?", "How many people have you been with?", "Has anyone ever accidentally seen you naked? Who?", "Have you ever gone out without wearing a bra and underwear?", "Who was your first crush?", "Have you ever had a crush on your teacher/professor?", "Have you ever had a crush on your best friend’s mom or someone generally much older that you?", "If you were the opposite gender for the day? What do you think you would wear? What would you do?", "If you and one person in this room could be the last people on Earth left alive, who would that person be?", "Who in this room do you think would be the worst date?", "Who in this room do you think would be the best date?", "What is your secret talent if you have one?", "What is the worst thing about being your gender?", "If you were a superhero, what would your power be?", "Have you ever performed a striptease for anyone before?", "Have you ever eaten food from the floor?", "What is the most trouble that you ever got into in school?", "What is the most trouble that you ever got into at home / with your parents?", "When was a time that someone really betrayed your trust?", "Talk about a time that you failed in life.", "Have you ever spread a rumor?", "Do you sing in the shower?", "When is the last time you threw up?", "When is the last time you cried?", "When is the last time you cried?", "What is the most embarrassing thing that you have ever done in front of a crush?", "What do you look for in a potential love interest?", "Would you rather be rich or famous? You cannot be both.", "Who is the most annoying person in the room?", "Which person in the room do you think gossips the most?", "What is your biggest insecurity?", "What is a common misconception about you?", ">Where is the weirdest place that you have gone to the bathroom?", ">What is the most embarrassing thing that your parents have caught you doing?", "What was the most disgusting thing to ever come out of your body?", "What is the most disgusting thing that you have ever had in your mouth?", " Have you ever wanted to have a one night stand?", "Have you ever wanted to kill someone?", "What is the worst thing that somebody ever said to you?", "What is your biggest fantasy?", "Have you ever gone to the bathroom in the pool?", "Who in the group do you think is the wildest in bed?", "For guys: have you ever worn lingerie?", "What is your idea of good sex?", "Do you masturbate?", "How many times do you take care of yourself a week?", "What is the most sex that you have had in a day?", "What is the longest amount of time that you have gone without intercourse?", "Have you ever received oral sex?", "Would you ever swap partners with anyone?", "Have you ever stolen money from your parents?", "Have you ever taken nude photos or videos of yourself?", "Could you live without watching “adult movies”?", "Could you live without having sex for the rest of your life?", "Have you ever stolen something for a store?", "What is an unpopular opinion that you have?", "If you weren’t here playing with us right now, what would you probably be doing?", "What kind of person would you want to marry one day?", "What do you think happens after we die?", "What is your favorite movie and why?", "What is the silliest thing that you have ever done?", "Who would play you in a movie about your life?", "Name one thing on your bucket list.", "If you could kiss one celebrity, who would it be?", ">If you could say anything to one person in your life without any consequences, what would it be?", "If you could choose a way to die, what would it be?", "How many romantic interests do you think you will have for the rest of your life?", "Was there ever a time in your life that you thought you were going to die?", "What is the most romantic thing that you have ever done?", "What is the most romantic thing that has ever been done for you?", "What is your most embarrassing puberty-related story?", "Where did you used to think babies come from?", "What is one thing that you have always wanted to do but have not gotten around to it yet?", "Have you ever let someone take the blame for something you did? What happened?", "Describe the last dream you had?", " If I went through your room, what would I be shocked to find?", "Have you ever flashed someone?", "Have you ever stalked someone on Facebook?", "Have you ever waited for my text message?", " How many boys/girls contact numbers are there on your phone?", " Tell me that one secret that you’re hiding from your mom?", "Is there anything in your life that you would change?", "How many people have you kissed?", "Have you ever practiced kissing the mirror?", "What was your most embarrassing moment in public?", "What is your guilty pleasure?", "Have you ever farted in an elevator?", "If you suddenly became invisible what would you do?", "Describe what your crush looks like", "Tell me about the last time you got really embarrassed.", "What is the weirdest food combo you’ve ever eaten?", "What is the last thing that made you cry?", "Who is the last person you tried to impress?", "If you had to be stranded on a deserted island with a celebrity, who would you choose?", "Tell your crush you like them over text and never respond back to her queries regarding it. Screenshot the conversation.", "Call someone and confess your new love of Justin Beiber",
                        "Write a short love poem", "Send me a picture of your first crush", "Set your crush's picture as your pfp.","If you could be someobe for a day who would it be", "Have you ever broke a promise to someone on purpose", " If you could eat ONE! food for a whole day only what would it be", "Did friends ever leave you", " If you could bring someone to a haunted house with you who would it be", "Have you ever ate something that isn't edible if so what was it", "What are your top three turn-ons?", "Tell me about your first kiss.", "Who was the last person you licked?", "Tell me about your most awkward date.", "What are you most self-conscious about?", " When was the last time you peed in bed?", "Who is the person you most regret kissing?", "Tell us your most embarrassing vomit story.", " What is the naughtiest thing you’ve done in public?", "What do most people think is true about you, but isn’t?", "What is the biggest thing you’ve gotten away with?", "What would you do if you were the opposite sex for a month?", "What is the most childish thing you still do?", "What is the most childish thing you still do?", "What is something your friends would never expect that you do?", " Who here would you most like to make out with?", "What lie have you told that hurt someone?", "What is the meanest you have been to someone that didn’t deserve it?", "What is something that people think you would never be into, but you are?", "What was the worst encounter you had with a police officer?", "What is the silliest thing you have an emotional attachment to?", "Where is the strangest place you have peed?", "What secret about yourself did you tell someone in confidence and then they told a lot of other people?", "When was the most inappropriate time you farted?", "What is the scariest dream you have ever had?", "Why did you break up with your last boyfriend or girlfriend?", "What is your favorite thing that your boyfriend or girlfriend does?", "What terrible thing have you done that you lied to cover up?", " Who have you loved but they didn’t love you back?", ". What is something that you have never told anyone?", " What is the most disgusting habit you have?", " What pictures or videos of you do you wish didn’t exist?", "What was the cruelest joke you played on someone?", "What is the most embarrassing thing you have put up on social media?", "What was the most awkward romantic encounter you have had?", "Tell me about the last time someone unexpectedly walked in on you while you were naked.", "What is the most embarrassing nickname you have ever had?", "What is the most embarrassing series of texts you have on your phone?", "Describe your most recent romantic encounter in detail.", " What is the weirdest thing you have done for a boyfriend or girlfriend?", "Is it true that you (whatever you or the group suspects they do / did)?", "Tell me something you don’t want me to know.", "What have you done that people here would judge you most for doing?", "If you starred in a romance, what would it be like?", "If you starred in a romance, what would it be like?", "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, which would you choose?", "Have you ever walked in on your parents doing it?", "What's the first thing you would do if you woke up one day as the opposite sex?", "Of the people in this room, who do you want to trade lives with?", "Have you ever had a wardrobe malfunction?", "Have you ever walked into a wall?", "You’re in a public restroom and just went #2, then you realized your stall has no toilet paper. What do you do?", "What would be in your web history that you’d be embarrassed if someone saw?", "Do you talk in your sleep?", "How often do you wash your undergarments?", "Have you ever tasted ear wax?", "Have you ever tasted your sweat?", "If you were allowed to marry more than one person, would you? Who would you choose to marry?", "Would you rather lose your sex organs forever or gain 200 pounds?", "Would you choose to save 100 people without anyone knowing about it or not save them but have everyone praise you for it?", "If you could only hear one song for the rest of your life, what would it be?", "If you lost one day of your life every time you said a swear word, would you try not to do it?", "Who in this room would be the worst person to date? Why?", "If someone offered you $1 million to break up with your girlfriend/boyfriend, would you do it?", "If you were reborn, what decade would you want to be born in?", "If you could go back in time in erase one thing you said or did, what would it be?", "Has your boyfriend or girlfriend ever embarrassed you?", "Have you ever thought about cheating on your partner?", "If you could suddenly become invisible, what would you do?", "Have you ever been caught checking someone out?", "Have you ever ding dong ditched someone?", "The world ends next week, and you can do anything you want (even if it's illegal). What would you do?", "Would you wear your shirt inside out for a whole day if someone paid you $100?", "How far would you go to land the guy or girl of your dreams?", "Tell us about a time you embarrassed yourself in front of a crush.", "Who is one person you pretend to like, but actually don’t?", "If you had to make out with any Animated character, who would it be?", "Have you ever watched a movie you knew you shouldn’t?", "What is the most food you’ve eaten in a single sitting?", "What ‘As seen on TV’ product do you secretly want to buy?", "If you were home by yourself all day, what would you do?", "What was the last R-rated movie you watched?", "Do you lick your plate?", "Would you rather go for a month without washing your hair or go for a day without wearing a bra?", "Have you ever had a crush on a person at least 10 years older than you?", "If you could marry any celebrity, who would it be?", "If you could marry any celebrity, who would it be?", "Who was your first kiss? Did you like it?", "Who are you jealous of?", "How many kids do you want to have in the future?", "Have you ever flirted with your best friend’s siblings?", "Jock, nerd, or bad guy/girl?", "Have you ever had a crush on friend's boyfriend?", "What's the sexiest thing about a guy/girl?", "If you could eat anything you wanted without getting fat, what would that food be?", "If you had to do a game show with someone in this room, who would you pick?", "Would you go a year without your phone if it meant you could marry the person of your dreams?", "Would you date someone shorter than you?", "If someone paid you $1000 to wear your bra outside your shirt, would you do it?", "What's the best thing to say to your friend that would be the worst thing to say to your crush?", "What's the best thing to say to your friend that would be the worst thing to say to your crush?", "If you had nine lives, what would you do that you wouldn't do now?", "If you could spend every waking moment with your gf or bf, would you?", "If your crush told you he liked your best friend, what would you do?", "What if your best friend told you that she liked your crush?", "If you had to date someone else's partner, who would it be?", "f you had to trade your friend in for the celebrity crush of your dreams, which friend would you choose?", "What do you think about him/her now?", "On an overnight trip, would you rather share a bed with your best friend or her boyfriend?", "If you could swap one physical feature with your best friend, what would that be?", "What is your crush's personality like?", "Is there anything about your life you would change?", "Would you rather be skinny and hairy or fat and smooth?", "Would you ever date two people at once if you could get away with it?", "If you had to choose between dating someone ugly who was good in bed or dating someone hot who was bad in bed, which would you choose?", "If you could make out with someone else's girl/guy, who would it be?", "If a girl you didn't like had a crush on you, how would you act around her?", "If you had to flash just one person in this room, who would it be?", "If you haven't had your first kiss yet, who in this room do you want to have your first kiss with?", "If you only had 24 hours to live and you could do anything with anyone in this room, who would it be and what would you do with that person?", "If you had to delete one app from your phone, which one would it be?", "What was a rumor that went around about you?", "Have you ever been in a 'friends with benefits' situation?", ""]

            randtruth = secrets.choice(truthlist)

        elif flag == 2:            
            source = requests.get("https://manofmany.com/entertainment/gaming/best-truth-or-dare-questions").text
            soup = bs4.BeautifulSoup(source, "lxml")
            article = soup.find("article", class_ = 'wrapper clearfix post-310107 post type-post status-publish format-standard has-post-thumbnail hentry category-gaming tag-games tag-lists tag-truth-or-dare')
            q = article.find('div', class_ = 'entry-content small-post clearfix')
            q2 = (q.div.ol.find_all('li'))

            try:
                q2 = q2[secrets.randbelow(84)]
                randtruth= q2.contents[0]
            
            except:
                randtruth = "Kill, Marry and Fuck whom in this server?"
        
        else:
            source = requests.get("https://funattic.com/301-truth-or-dare-questions/").text
            soup = bs4.BeautifulSoup(source, "lxml")
            article = soup.find("article", itemtype ="https://schema.org/BlogPosting")

            q = article.find('div', class_ = 'entry-content')
            q1 = q.find_all('ol')
            x = secrets.randbelow(3)

            if x == 0:
                q2 = q1[x].find_all('li')[secrets.randbelow(166)]

            elif x == 1:
                q2 = q1[x].find_all('li')[secrets.randbelow(167)]

            else: 
                q2 = q1[x].find_all('li')[secrets.randbelow(19)]

            try:
                randtruth= q2.contents[0]
            
            except:
                randtruth = "Kill, Marry and Fuck whom in this server?"



        phraselist = ["ask 'em this!", "here's a question:", "go embarrass them.", "Ooolalaaa~", "boom!", "it doesn't feel good aye?", "let's show no empathy"]
        randphrase = secrets.choice(phraselist)

        await ctx.send(f"<@{ctx.author.id}> {randphrase} **{randtruth}**")

        

    
    @commands.command()
    async def d(self, ctx):

        darelist = ["Pledge your undying love to the person directly to your love interest for a minute(in VC).", "Make an unflattering picture of yourself your Discord pfp for a day.", "Pick up a random book and read it in the most seductive voice you can manage.", """Change your Discord status to “I’m coming . . . I’m coming . . ." Then, 12 hours later, change it to "I just came." """, "Do your best sexy moan.", "Use a pickup line on one of us.", "Say something very dirty to one us in the server", "Send a love letter to someone of the opposite sex, and never reveal to the other person that it was a dare", "Give an insult to every person in the room", "Show your whole browsing history to the players in the room.", ">Disclose your girlfriend’s/boyfriend’s name.", "Behave like a lesbian for the rest of the game.", "Show the most embarrassing photo on your phone.", "Send a sext to the last person in your phonebook.", "Say two honest things about everyone else in the group.", "Serenade the person to your right.", "Post an extremely unflattering picture of yourself to the social media outlet of your choosing.", "Send me the last YouTube video you watched.", "Put my picture as your phone wallpaper for three days.", "Call me and say “I Love You” along with my name as loud as you can.", "Send me a screenshot of your Whatsapp chat list immediately.", "Send me the dirtiest text message you can think of.", " Send a romantic text to someone of your own gender and tell me the results.", "Tell me a fantasy you’ve never told anyone."]
        
        randdare = secrets.choice(darelist)

        phraselist = ["ask 'em this!", "here's a question:", "go embarrass them.", "Ooolalaaa~", "boom!", "it doesn't feel good aye?", "let's show no empathy"]
        randphrase = secrets.choice(phraselist)

        await ctx.send(f"<@{ctx.author.id}> {randphrase} **{randdare}**")


    
def setup(bot):
    bot.add_cog(TruthDare(bot))