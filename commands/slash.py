from hata import sleep, Embed, Color, Emoji
from random import random, choice
import os, re

# emotes
CAT_FISH = Emoji.precreate(os.environ.get('CAT_FISH'))
CAT_SAD = Emoji.precreate(os.environ.get('CAT_SAD'))
CAT_WAY = Emoji.precreate(os.environ.get('CAT_WAY'))
NEKOGIRL_KISS = Emoji.precreate(os.environ.get("NEKOGIRL_KISS"))
NEKOGIRL_PEEK = Emoji.precreate(os.environ.get('NEKOGIRL_PEEK'))

# colors
CAT_FACT_COLOR = Color.from_html('#F6D33C')
OwO_COLOR = Color.from_html('#FF69B4')
NEKOGIRL_COLOR = Color.from_html('#FFB6C1')
CAT_COLOR = Color.from_html('#000000')

# data
CAT_FACTS = [
        "A house cat’s genome is 95.6 percent tiger, and they share many behaviors with their jungle ancestors, says Layla Morgan Wilde, a cat behavior expert and the founder of Cat Wisdom 101. These behaviors include scent marking by scratching, prey play, prey stalking, pouncing, chinning, and urine marking.",
        "Cats are believed to be the only mammals who don’t taste sweetness.",
        "Cats are nearsighted, but their peripheral vision and night vision are much better than that of humans.",
        "Cats are supposed to have 18 toes (five toes on each front paw; four toes on each back paw).",
        "Cats can jump up to six times their length.",
        "Cats’ claws all curve downward, which means that they can’t climb down trees head-first. Instead, they have to back down the trunk.",
        "Cats’ collarbones don’t connect to their other bones, as these bones are buried in their shoulder muscles.",
        "Cats have 230 bones, while humans only have 206.",
        "Cats have an extra organ that allows them to taste scents on the air, which is why your cat stares at you with her mouth open from time to time.",
        "Cats have whiskers on the backs of their front legs, as well.",
        "Cats have nearly twice the amount of neurons in their cerebral cortex as dogs.",
        "Cats have the largest eyes relative to their head size of any mammal.",
        "Cats make very little noise when they walk around. The thick, soft pads on their paws allow them to sneak up on their prey — or you!",
        "Cats’ rough tongues can lick a bone clean of any shred of meat.",
        "Cats use their long tails to balance themselves when they’re jumping or walking along narrow ledges.",
        "Cats use their whiskers to “feel” the world around them in an effort to determine which small spaces they can fit into. A cat’s whiskers are generally about the same width as its body. (This is why you should never, EVER cut their whiskers.)",
        "Cats walk like camels and giraffes: They move both of their right feet first, then move both of their left feet. No other animals walk this way.",
        "Male cats are more likely to be left-pawed, while female cats are more likely to be right-pawed.",
        "Though cats can notice the fast movements of their prey, it often seems to them that slow-moving objects are actually stagnant.",
        "Some cats are ambidextrous, but 40 percent are either left- or right-pawed.",
        "Some cats can swim.",
        "There are cats who have more than 18 toes. These extra-digit felines are referred to as being “polydactyl.”",
        "A cat’s learning style is about the same as a 2- to 3-year-old child.",
        "A cat’s purr vibrates at a frequency of 25 to 150 hertz, which is the same frequency at which muscles and bones repair themselves.",
        "A group of kittens is called a “kindle.”",
        "A house cat could beat superstar runner Usain Bolt in the 200 meter dash.",
        "About half of the cats in the world respond to the scent of catnip.",
        "Cat breeders are called “catteries.”",
        "Cats can be toilet-trained.",
        "Cats can drink sea water in order to survive. (In case you’re wondering, we can’t.)",
        "Cats don’t have an incest taboo, so they may choose to mate with their brothers and sisters.",
        "Cats dream, just like people do.",
        "Cats have contributed to the extinction of 33 different species.",
        "Cats perceive people as big, hairless cats, says Wilde.",
        "Cats were first brought to the Americas in colonial times to get rid of rodents.",
        "Collective nouns for adult cats include “clowder,” “clutter,” “glaring,” and “pounce.”",
        "I don't know anything about cats",
        "Each cat’s nose print is unique, much like human fingerprints.",
        "Every Scottish Fold cat in the world can trace its heritage back to the first one, which was found in Scotland in the 1960s, says Cheryl Hogan, a Scottish Fold breeder and the committee chair for the breed at The International Cat Association (TICA).",
        "It’s not uncommon to see cats in food stores in big cities as a form of free — and adorable — pest control.",
        "Kittens in the same litter can have more than one father. This is because the female cat releases multiple eggs over the course of a few days when she is in heat.",
        "Male cats are the most sensitive to catnip, while kittens under 3 months old have no response at all.",
        "Most world languages have a similar word to describe the “meow” sound.",
        "People often think that they’ve stumbled over a purebred as a stray or in a shelter, but Hogan says that this is very uncommon. “Ninety-nine times out of 100 what you have found on the street will not be purebred anything,” she says. “Very seldom do breeders sell kittens that are not already spayed or neutered,” as purebred cats need to meet very strict standards.",
        "Some 700 million feral cats live in the United States, and many shelters run trap-neuter-release programs to stem the population growth.",
        "Studies suggest that domesticated cats first appeared around 3600 B.C.",
        "The first known cat video was recorded in 1894.",
        "There are about 88 million pet cats in the United States, which makes them the most popular pet in the country!",
        "Two hundred feral cats prowl the park at Disneyland, doing their part to control rodents — the ones who don’t wear funny outfits and speak in squeaky voices.",
        "White cats with blue eyes are prone to deafness.",
        "A green cat was born in Denmark in 1995. Some people believe that high levels of copper in the water pipes nearby may have given his fur a verdigris effect.",
        "It turns out that Abraham Lincoln was a crazy cat president! He had four cats that lived in the White House with him.",
        "Maria Assunta left her cat, Tomasso, her entire $13 million fortune when she died in 2011.",
        "President Bill Clinton’s cat, Socks, was a media darling during the Clinton administration and was said to receive more letters than the President himself.",
        "Stubbs, a 17-year-old orange tabby, is mayor of the historic district of Talkeetna, Alaska.",
        "HuyaneMatsu is a nekogirl and she loves Nyansia",
        "sunday is a naughty cat",
        "A cat’s average lifespan increased by a year over the span of time between 2002 and 2012, according to a study by Banfield Pet Hospital.",
        "According to The Huffington Post, cats typically sleep for 12 to 16 hours a day.",
        "Cats are crepuscular, which means that they’re most active at dawn and dusk.",
        "Cats are fastidious creatures about their “bathroom.” If you have more than one cat, you should have one litter box for each.",
        "Cats can spend up to a third of their waking hours grooming.",
        "Cats live longer when they stay indoors.",
        "Cats’ purring may be a self-soothing behavior, since they make this noise when they’re ill or distressed, as well as when they’re happy.",
        "Cats will refuse an unpalatable food to the point of starvation.",
        "Despite popular belief, many cats are actually lactose intolerant.",
        "Female cats have the ability to get pregnant when they are only 4 months old!",
        "Grapes and raisins, as well as onions, garlic, and chives, are all extremely harmful foods for cats. Grapes and raisins can cause kidney failure — although the reasoning behind that isn’t clear. Meanwhile, onions, garlic, and chives wreak havoc on your cat’s gastrointestinal system and can cause anemia.",
        "If you keep your cat active during the day, he will sleep better at night. If you’re not free-feeding your cat, you can also help her get a good night’s sleep by providing her with a substantial evening meal.",
        "It’s believed that catnip produces an effect similar to LSD or marijuana in cats. The effects of nepetalactone — the chemical in catnip that can makes cats crazy — wears off within 15 minutes, and won’t surface again for a few hours, even if your cat remains in sniffing distance.",
        "Kittens can be spayed or neutered when they are only eight weeks old. If possible, these procedures should be performed in the first 5 months of your cat’s life.",
        "Male cats who have been fixed need fewer calories to maintain their weight.",
        "Spaying and neutering can extend a cat’s life. The Banfield Pet Hospital study found that neutered males live an average of 62 percent longer than unneutered cats and spayed females live an average of 39 percent longer than unspayed cats.",
        "Your cat’s grooming process stimulates blood flow to his skin, regulates his body temperature and helps him relax.",
        "A cat with a question-mark-shaped tail is asking, “Want to play?”",
        "According to Wilde, a slow blink is a “kitty kiss.” This movement shows contentment and trust.",
        "Cats have a unique “vocabulary” with their owner — each cat has a different set of vocalizations, purrs and behaviors.",
        "Cats have up to 100 different vocalizations — dogs only have 10.",
        "Cats find it threatening when you make direct eye contact with them.",
        "Cats mark you as their territory when they rub their faces and bodies against you, as they have scent glands in those areas.",
        "Cats may yawn as a way to end a confrontation with another animal. Think of it as their “talk to the hand” gesture.",
        "Hissing is defensive, not aggressive, says Wilde. “It’s an expression of fear, stress or discomfort of a threatened cat communicating ‘stay away,'” she says.",
        "If cats are fighting, the cat that’s hissing is the more vulnerable one, says Wilde.",
        "If your cat approaches you with a straight, almost vibrating tail, this means that she is extremely happy to see you.",
        "Kneading — which some people refer to as “making biscuits” — is a sign of contentment and happiness. Cats knead their mothers when they are nursing to stimulate the let-down of milk.",
        "Meowing is a behavior that cats developed exclusively to communicate with people.",
        "When a cat flops over and exposes his belly, it’s not always an invitation for a belly rub. A cat does this when he’s relaxed and showing trust.",
        "When cats hit you with retracted claws, they’re playing, not attacking.",
        "When dogs wag their tails, they may be expressing happiness. But this isn’t the case for cats! When your cat wags her tail, it’s her way of warning you that you are getting on her last nerve.",
        "When your cat sticks his butt in your face, he is doing so as a gesture of friendship.",
        "Whiskers are also good indicators of a cat’s mood. When a cat is scared, he put his whiskers back. But when a cat is in hunting mode, he puts his whiskers forward.",
        "Your cat drapes its tail over another cat, your dog, or you as a symbol of friendship.",
        "Cats are very fussy about their water bowls; some prefer to ignore their bowls entirely in favor of drinking from the sink faucet.",
        "Cats groom other cats — and sometimes people — in a ritual called allogrooming.",
        "Cats like to sleep on things that smell like their owners, such as their pillows and dirty laundry (ick!).",
        "Cats love to sleep in laundry baskets, too, because they’re basically hiding places with peep holes.",
        "Cats often attack your ankles when they’re bored.",
        "Certain cats go crazy for foods you wouldn’t expect, like olives, potato chips, and the hops in beer.",
        "For some reason, cats really dislike citrus scents.",
        "If you can’t find your cat, you should look in a box or a bag, as these are some of their favorite hiding spots!",
        "Male cats who try to get to a female in heat can show very bizarre behavior — for example, some have been known to slide down chimneys!",
        "Many cats like to lick their owner’s freshly washed hair.",
        "Some cats love the smell of chlorine.",
        "Thieving behavior is not uncommon among cats. They will often grab objects like stuffed animals, feather dusters, and other things that remind them of prey.",
        "In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.",
        "Cats can rotate their ears 180 degrees.",
        "The hearing of the average cat is at least five times keener than that of a human adult.",
        "In the largest cat breed, the average male weighs approximately 20 pounds.",
        "Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.",
        "A cat cannot see directly under its nose.",
        "Most cats have no eyelashes.",
        "Cats have five toes on each front paw, but only four on the back ones. It’s not uncommon, though, for cats to have extra toes. The cat with the most toes known had 32—eight on each paw!",
        "Some believe that if you dream about a white cat, good luck will follow.",
        "Meows are not innate cat language—they developed them to communicate with humans!",

    ]

# API
BASE_URL = 'https://nekos.life/api/v2'
HTTP = Pichu.http

# owoify text
_str_emojis = [
    "꒰◍ᐡᐤᐡ◍꒱",
    "{ @❛ꈊ❛@ }",
    "6(◦･ω･◦)9",
    "UwU",
    "OwO",
    "@w@",
    "◕w◕"
]

def owo(*, txt: str, ending_emoji: bool = False) -> str:
    """
    `txt`: The text you wish to 'owoify'
    `ending_emoji`: Whether you wish to add an
    emoji at the end of your text to make it 
    especially stand out 
    """

    replacements = {
        r"(?:l|r)": "w",
        r'(?:L|R)': "W",
        r'n([aeiou])': "ny",
        r'N([aeiou])|N(AEIOU)': "Ny",
        r"ove": "uv",
        r'nd(?= |$)': "ndo"
    }

    for pattern, replacement in list(replacements.items()):
        txt = re.sub(pattern=pattern, repl=replacement, string=txt)

    if ending_emoji:
        txt += " " + choice(_str_emojis)

    return txt


@Pichu.interactions(is_global=True)
async def cat(client, event):
    """I will be good neko! moo!"""
    try:
        async with HTTP.get(BASE_URL+'/img/meow') as response:
            if response.status != 200:
                return "Couldn't contact the API right now..."
            data = await response.json()
        return Embed(f"Here is your cat {CAT_FISH:e}", color=CAT_COLOR).\
            add_image(data['url'])
    except (OSError, ConnectionError):
        return None


@Pichu.interactions(is_global=True)
async def catfact(client, event, search: ('str', 'search using the keyword') = None):
    """ask me purrr!"""

    if search is None:
        yield Embed(f"Here is your cat fact {CAT_WAY:e}", description=choice(CAT_FACTS), color=CAT_FACT_COLOR)

    else:
        # bot is thinking... :p
        yield "*Thinking...*"
        await sleep(1.0 + random.random() * 4.0)
        await client.interaction_response_message_delete(event)

        # finding the possible facts by using the keyword
        matching = [s for s in CAT_FACTS if search in s]

        if matching:
            yield Embed(f"Here is your cat fact {CAT_WAY:e}", description=choice(matching), color=CAT_FACT_COLOR)

        else:
            yield f"{CAT_SAD:e} sowwy, couldn't find"


@Pichu.interactions(is_global=True)
async def nekogirl(client, event):
    """wanna see nekogirls? OwO"""
    try:
        async with HTTP.get(BASE_URL+'/img/neko') as response:
            if response.status != 200:
                return "Couldn't contact the API right now..."
            data = await response.json()
        return Embed(f"Here is your nekogirl {NEKOGIRL_KISS:e}", color=NEKOGIRL_COLOR).\
            add_image(data['url'])
    except (OSError, ConnectionError):
        return None
        

@Pichu.interactions(is_global=True)
async def owoify(client, event, text: ('str', 'Please, enter the message OwO')):
    """owoified text"""
    
    return Embed( color=OwO_COLOR).\
        add_field(f"OwOified Text {NEKOGIRL_PEEK:e}", owo(txt=text, ending_emoji=True)).\
        add_footer("purrr!!!")


@Pichu.interactions(is_global=True)
async def textcat(client, event):
    """I will send textcats :3"""
    try:
        async with HTTP.get(BASE_URL+'/cat') as response:
            if response.status != 200:
                return "Couldn't contact the API right now... OwO"
            data = await response.json()
        return data['cat']
    except (OSError, ConnectionError):
        return None


@Pichu.interactions(is_global=True)
async def why(client, event):
    """why are you using this commands?"""
    try:
        async with HTTP.get(BASE_URL+'/why') as response:
            if response.status != 200:
                return "Couldn't contact the API right now... WHY?"
            data = await response.json()
        return data['why']
    except (OSError, ConnectionError):
        return None

