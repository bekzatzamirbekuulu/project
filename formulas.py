from rubikscube import bot, dp
from aiogram.types import Message
from config import Admin_id
from inline import cube
async def send_to_admin(dp):
    await bot.send_message(chat_id=Admin_id, text="Bot is started")


@dp.message_handler()
async def send_formulas(message: Message):
    if message.text.lower() == "/start":
        await bot.send_message(chat_id=message.from_user.id, text=""
                                                                  "To solve "
                                                                  "the"
                                                                  " Rubik's "
                                                                  "cube quick"
                                                                  "ly"
                                                                  " you need "
                                                                  "to learn"
                                                                  " a lot of "
                                                                  "rules. An"
                                                                  "d "
                                                                  "these rule"
                                                                  "s "
                                                                  "are made u"
                                                                  "p "
                                                                  "of "
                                                                  "letters."
                                                                  " For"
                                                                  " example "
                                                                  "the"
                                                                  " formula "
                                                                  "of "
                                                                  "a fish: "
                                                                  "R U R'U R "
                                                                  "U2"
                                                                  " R'")
        await message.answer("And I need to know: do you know what do mean "
                             "this"
                             " letters in formula?"
                             "\nIf you can, click '/iknow'\n"
                             "if cannot, then click "
                             "'/idonotknow'", reply_markup=cube)
    elif message.text.lower() == "/idonotknow":
        await message.answer("OK, let's start! In the following message I "
                             "will "
                             "tell you what do mean this letters.")
        await message.answer("R - means right side of the cube\nSmall r - "
                             "means"
                             " two right layers\n"
                             "L - means left side of the cube\nSmall l -"
                             " means "
                             "two left layers\n"
                             "U - means upper side of the cube\nSmall u - "
                             "means"
                             " two upper layers\n"
                             "D - means down side of the cube\nSmall d -"
                             " means "
                             "two down layers\n"
                             "F - means front side of the cube(front is the "
                             "side that is opposite you)\n"
                             "Small f - means two front layers\n"
                             "B - means back side of the cube\nSmall b -"
                             " means "
                             "two left layers\n"
                             "M - means middle side\n")
        await message.answer("When you have finished learn what do mean the "
                             "letters then click \n'/next'")
    if message.text.lower() == "/next":
        await message.answer("After you should learn, how to rotate the "
                             "sides.")
        await message.answer("A single letter by itself refers to a clockwise "
                             "face rotation in 90 degrees (quarter turn)"
                             ". "
                             "REMEMBER! The sides will rotate relative to "
                             "itself. "
                             "And if the letter will stay with quotation "
                             "mark, "
                             "side will rotate "
                             "counterclockwise. There is a one letter maybe "
                             "will do confused you. "
                             "This is letter is M. Because you don't know "
                             "where"
                             " to look at the middle "
                             "layer to the right or left. I just will say you "
                             "how it is rotates.\nM means you should "
                             "rotate middle layer to up, M' means you should "
                             "rotate to down.\n"
                             "If the letter will stay with number 2, then "
                             "this "
                             "side will rotate two times."
                             "That means the formula will be like that:\nR2 = "
                             "R + R or R2 = R' + R'. "
                             "it doesn't matter which of these options you "
                             "will"
                             " use.")
        await message.answer("And also there 3 letters that you should know: "
                             "x, y, z.\n"
                             "x - rotate the entire cube on R (do an R move "
                             "without holding the "
                             "two other layers)\n"
                             "y - rotate the entire cube on U\n"
                             "z - rotate the entire cube on F\n"
                             "And last one what you should to know:\nif with "
                             "this three letters"
                             "will stay quotation mark, then the rotation "
                             "will "
                             "change to opposite"
                             "direction")
        await message.answer("When you have learned all of the above click "
                             "'/iknow'")
    elif message.text.lower() == "/iknow":
        await message.answer("The Rubik's cube assembly consists"
                             " of four parts.")
        await message.answer("There are:\ncross "
                             "https://ruwix.com/pics/fridrich/01-cross.png")
        await message.answer("F2L(solving the first two layers) "
                             "https://ruwix.com/pics/fridrich/02-f2l.png")
        await message.answer("OLL(orientation of last layer) "
                             "https://ruwix.com/pics/fridrich/03-oll.png")
        await message.answer("PLL(permutation of last layer) "
                             "https://ruwix.com/pics/fridrich/04-pll.png")
        await message.answer("Cross is solving intuitively. You should "
                             "collect "
                             "white cross on the white center,"
                             " and you must collect the cross with the white "
                             "center down. In addition, I can give "
                             "you some advice how to increase speed of "
                             "solving "
                             "a cross.")
        await message.answer("1. Remember the arrangement of the cube colors. "
                             "For example, blue has red on the right, "
                             "red has green on the right, green has orange, "
                             "etc.\n"
                             "2. Collect a white cross less then eight "
                             "moves.\n"
                             "3. Train to solve the cross blindly, "
                             "remembering "
                             "where the ribs are. It will "
                             "help you immediately see the ribs and "
                             "understand "
                             "how to assemble the cross.\n"
                             "If you had learned hot to solve a cross, then "
                             "print this button \n➡  '/gotof2l'")
    elif message.text.lower() == "/gotof2l":
        await message.answer("F2L is the part of the Rubik's cube in which "
                             "the "
                             "first two layers are assembled at once."
                             " So you need to collect the corner and its "
                             "adjacent edge at once"
                             "F2L can be solved intuitively and with "
                             "formulas. "
                             "I will give you formulas. "
                             "You just have to check the situations and"
                             " follow "
                             "the formulas that I will give you now")
        await message.answer("For beginning I will give you first 'Easy "
                             "cases' "
                             "four F2L formulas:\n"
                             "https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "01.png\n"
                             "R U R'")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "17.png\n"
                             "F'U'F")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "19.png\n"
                             "U' F' U F")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "18.png\n"
                             "U R U' R'")
        await message.answer("To go to the next step click '/secondstep'")
    elif message.text.lower() == "/secondstep":
        await message.answer("Second case is 'Corner in bottom, edge in top "
                             "layer'\n"
                             "https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "38.png\n"
                             "(U R U' R') (U' F' U F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "39.png\n"
                             "(U' F' U F) (U R U' R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "40.png\n"
                             "(F' U F) (U' F' U F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "42.png\n"
                             "(R U R') (U' R U R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "41.png\n"
                             "(R U' R') (U R U' R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "43.png\n"
                             "(F' U' F) (U F' U' F)")
        await message.answer("Go to next step by clicking '/thirdstep'")
    elif message.text.lower() == "/thirdstep":
        await message.answer("Third case is 'Corner in top, edge in middle'\n"
                             "https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "12.png\n"
                             "(R U R' U') (R U R' U') (R U R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "48.png\n"
                             "(R U' R') (d R' U R)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "44.png\n"
                             "(U F' U F) (U F' U2 F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "46.png\n"
                             "(U F' U' F) (d' F U F')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "45.png\n"
                             "(U' R U' R') (U' R U2 R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "47.png\n"
                             "(U' R U R') (d R' U' R)")
        await message.answer("click this ➡ '/fourthstep' to go to next step")
    elif message.text.lower() == "/fourthstep":
        await message.answer("Fourth case is 'Corner pointing outwards, edge"
                             " in"
                             " top layer'\n"
                             "https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "26.png\n"
                             "(R U' R' U) (d R' U' R)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "27.png\n"
                             "(F' U F U') (d' F U F')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "28.png\n"
                             "(U F' U2 F) (U F' U2 F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "29.png\n"
                             "(U' R U2 R') (U' R U2 R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "30.png\n"
                             "(U F' U' F) (U F' U2 F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "31.png\n"
                             "(U' R U R') (U' R U2 R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "20.png\n"
                             "(U' R U' R' U) (R U R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "21.png\n"
                             "(U F' U F U') (F' U' F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "22.png\n"
                             "(U' R U R' U) (R U R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "23.png\n"
                             "(U F' U' F U') (F' U' F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "24.png\n"
                             "(U F' U2 F U') (R U R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "25.png\n"
                             "(U' R U2 R' U) (F' U' F)")
        await message.answer("'/fifthstep' is the button to go next step")
    elif message.text.lower() == "/fifthstep":
        await message.answer("Fifth case is 'Corner pointing upwards, edge in "
                             "top layer'\n"
                             "https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "13.png\n"
                             "(R U R' U') U' (R U R' U') (R U R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "14.png\n"
                             "y' (R' U' R U) U (R' U' R U) (R' U' R)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "36.png\n"
                             "(U2 R U R') (U R U' R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "37.png\n"
                             "(U2 F' U' F) (U' F' U F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "34.png\n"
                             "(U R U2 R') (U R U' R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "35.png\n"
                             "(U' F' U2 F) (U' F' U F)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "32.png\n"
                             "(R U2 R') (U' R U R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "33.png\n"
                             "(F' U2 F) (U F' U' F)")
        await message.answer("next step is '/sixthstep'")
    elif message.text.lower() == "/sixthstep":
        await message.answer("Sixth case is 'Corner in bottom, edge in "
                             "middle'\n"
                             "https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "51.png\n"
                             "(R U' R' d R' U2 R) (U R' U2 R)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "49.png\n"
                             "(R U' R' U R U2 R') (U R U' R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "50.png\n"
                             "(R U' R' U' R U R') (U' R U2 R')")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "15.png\n"
                             "(R U R' U' R U' R') (U d R' U' R)")
        await message.answer("https://ruwix.com/pics/friedrich/friedrich-f2l-"
                             "16.png\n"
                             "(R U' R' d R' U' R) (U' R' U' R)")
        await message.answer("In all of the above formulas, I gave you "
                             "examples"
                             " only with blue-red elements. "
                             "This does not mean that these formulas are "
                             "suitable only for these colors, but you can"
                             " also compare these cases and if something "
                             "turned"
                             " out to be in a similar situation, then"
                             " follow the desired formula. This formulas will "
                             "be same if in the cube will be the "
                             "situation like on the picture:\nhttp://"
                             "badmephisto.com/pictures/f2l_open_slots.png")
        await message.answer("When you had learned all F2L formulas click "
                             "this "
                             "➡ '/gotooll'")
    elif message.text.lower() == "/gotooll":
        await message.answer("For convenience, I divided the formulas into "
                             "groups. In OLL 14 groups, but don't "
                             "be afraid. Because most of them are pretty "
                             "simple. This 14 groups are:\n"
                             "Dots\nLines\nCrosses\nFour corners\nShape _| or "
                             "Shape1\nShape |_ or Shape2\nShape |_ or "
                             "Shape3"
                             "\nShape |¯ or Shape4\n"
                             "C letters\nL letters\nP letters\nT letters\nW "
                             "letters\nAnd last Z letters\n"
                             "And also you have to do these formulas by "
                             "taking "
                             "a Rubik's cube as shown in the picture.")
        await message.answer("If you ready then click '/dots' to begin")
    elif message.text.lower() == "/dots":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "16.png\n"
                             "R U2 R2' F R F' U2' R' F R F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "17.png\n"
                             "F R U R' U' F' f R U R' U' f'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "18.png\n"
                             "y L' R2 B R' B L U2' L' B M'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "19.png\n"
                             "R' U2 x R' U R U' y R' U' R' U R' F")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "22.png\n"
                             "(R U R' U) R' F R F' U2 R' F R F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "23.png\n"
                             "M' U2 M U2 M' U M U2 M' U2 M")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "20.png\n"
                             "R' U2 F (R U R' U') y' R2 U2 x' R U")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "21.png\n"
                             "F (R U R' U) y' R' U2 (R' F R F')")
        await message.answer("Next step is '/lines'")
    elif message.text.lower() == "/lines":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "45.png\n"
                             "R' U' y L' U L' y' L F L' F R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "44.png\n"
                             "R U' y R2 D R' U2 R D' R2 d R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "46.png\n"
                             "F U R U' R' U R U' R' F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "47.png\n"
                             "L' B' L U' R' U R U' R' U R L' B L")
        await message.answer("Next is '/crosses'")
    elif message.text.lower() == "/crosses":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "11.png\n"
                             "L U' R' U L' U (R U R' U) R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "12.png\n"
                             "(R U R' U) R U' R' U R U2 R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "10.png\n"
                             "L' U R U' L U R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "09.png\n"
                             "R' U2 (R U R' U) R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "13.png\n"
                             "R' F' L F R F' L' F")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "15.png\n"
                             "R2 D R' U2 R D' R' U2 R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "14.png\n"
                             "R' F' L' F R F' L F")
        await message.answer("Next is '/fourcorners'")
    elif message.text.lower() == "/fourcorners":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "08.png\n"
                             "M' U' M U2' M' U' M")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "07.png\n"
                             "L' (R U R' U') L R' F R F'")
        await message.answer("Next is '/shape1'")
    elif message.text.lower() == "/shape1":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "30.png\n"
                             "L F R' F R F2 L'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "41.png\n"
                             "F R' F' R U R U' R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "35.png\n"
                             "R' U' R y' x' R U' R' F R U R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "38.png\n"
                             "U' R U2' R' U' R U' R2 y' R' U' R U B")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "24.png\n"
                             "F (R U R' U') (R U R' U') F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "29.png\n"
                             "L F' L' F U2 L2 y' L F L' F")
        await message.answer("Next is '/shape2'")
    elif message.text.lower() == "/shape2":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "39.png\n"
                             "U' R' U2 (R U R' U) R2 y (R U R' U') F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "43.png\n"
                             "r U2 R' U' R U' r'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "40.png\n"
                             "R' U2 l R U' R' U l' U2 R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "25.png\n"
                             "F' L' U' L U L' U' L U F")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "27.png\n"
                             "R' F R' F' R2 U2 x' U' R U R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "28.png\n"
                             "R' F R F' U2 R2 y R' F' R F'")
        await message.answer("Next is '/shape3'")
    elif message.text.lower() == "/shape3":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "36.png\n"
                             "R U R' y R' F R U' R' F' R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "31.png\n"
                             "L' B' L U' R' U R L' B L")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "32.png\n"
                             "U2 r R2' U' R U' R' U2 R U' M")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "34.png\n"
                             "x' U' R U' R2' F x (R U R' U') R B2")
        await message.answer("Next is '/shape4'")
    elif message.text.lower() == "/shape4":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "26.png\n"
                             "L U' y' R' U2' R' U R U' R U2 R d' L'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "33.png\n"
                             "U2 l' L2 U L' U L U2 L' U M")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "37.png\n"
                             "R2' U R' B' R U' R2' U l U l'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "42.png\n"
                             "r' U2 (R U R' U) r")
        await message.answer("Next is '/c'")
    elif message.text.lower() == "/c":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "05.png\n"
                             "R U x' R U' R' U x U' R'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "06.png\n"
                             "(R U R' U') x D' R' U R E'")
        await message.answer("Next is '/l'")
    elif message.text.lower() == "/l":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "01.png\n"
                             "R' F R U R' F' R y L U' L'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "02.png\n"
                             "L F' L' U' L F L' y' R' U R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "04.png\n"
                             "L' B' L R' U' R U L' B L")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "03.png\n"
                             "R B R' L U L' U' R B' R'")
        await message.answer("Next is '/p'")
    elif message.text.lower() == "/p":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "50.png\n"
                             "F U R U' R' F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "49.png\n"
                             "R' d' L d R U' R' F' R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "48.png\n"
                             "L d R' d' L' U L F L'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "51.png\n"
                             "F' U' L' U L F")
        await message.answer("Next is '/t'")
    elif message.text.lower() == "/t":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "52.png\n"
                             "F (R U R' U') F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "53.png\n"
                             "(R U R' U') R' F R F'")
        await message.answer("Next is '/w'")
    elif message.text.lower() == "/w":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "54.png\n"
                             "L U L' U L U' L' U' y2' R' F R F'")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "55.png\n"
                             "R' U' R U' R' U R U y F R' F' R")
        await message.answer("Next is '/z'")
    elif message.text.lower() == "/z":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "56.png\n"
                             "R' F (R U R' U') y L' d R")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-oll-"
                             "57.png\n"
                             "L F' L' U' L U y' R d' L'")
        await message.answer("To go to PLL part click this button '/gotopll'")
    if message.text.lower() == "/gotopll":
        await message.answer("I divided PLL formulas for convenience:\n"
                             "A-perms\nU-perms\nH-perm\nT-perm\nJ-perms\nR-"
                             "perms\nV-perm\nF-perm\nZ-perm\n"
                             "Y-perm\nN-perms\nE-perm\nG-perms")
        await message.answer("To start I will give you A-perms."
                             "https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "01.png\n"
                             "x [(R' U R') D2] [(R U' R') D2] R2")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "02.png\n"
                             "x' [(R U' R) D2] [(R' U R) D2] R2")
        await message.answer("Next perms are '/uperms'")
    elif message.text.lower() == "/uperms":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "07.png\n"
                             "R2 U [R U R' U'] (R' U') (R' U R')")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "06.png\n"
                             "[R U'] [R U] [R U] [R U'] R' U' R2")
        await message.answer("Next is '/hperm'")
    elif message.text.lower() == "/hperm":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "05.png\n"
                             "M2 U M2 U2 M2 U M2")
        await message.answer("Next is '/tperm'")
    elif message.text.lower() == "/tperm":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "10.png\n"
                             "[R U R' U'] [R' F] [R2 U' R'] U' [R U R' F']")
        await message.answer("Next are '/jperms'")
    elif message.text.lower() == "/jperms":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "08.png\n"
                             "[R' U L'] [U2 R U' R' U2] [R L U']")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "09.png\n"
                             "[R U R' F'] {[R U R' U'] [R' F] [R2 U' R'] U'}")
        await message.answer("Next are '/rperms'")
    elif message.text.lower() == "/rperms":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "12.png\n"
                             "[L U2' L' U2'] [L F'] [L' U' L U] [L F] L2' U")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "11.png\n"
                             "[R' U2 R U2] [R' F] [R U R' U'] [R' F'] R2 U'")
        await message.answer("Next is ''/vperm")
    elif message.text.lower() == "/vperm":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "18.png\n"
                             "[R' U R' d'] [R' F'] [R2 U' R' U] [R' F R F]")
        await message.answer("Next is '/fperm'")
    elif message.text.lower() == "/fperm":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "13.png\n"
                             "[R' U2 R' d'] [R' F'] [R2 U' R' U] [R' F R "
                             "U' F]")
        await message.answer("Next is '/zperm'")
    elif message.text.lower() == "/zperm":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "04.png\n"
                             "M2 U M2 U M' U2 M2 U2 M' U2")
        await message.answer("Next is '/yperm'")
    elif message.text.lower() == "/yperm":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "21.png\n"
                             "F R U' R' U' [R U R' F'] {[R U R' U'] [R' "
                             "F R F']}")
        await message.answer("Next are '/nperms'")
    elif message.text.lower() == "/nperms":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "19.png\n"
                             "{(L U' R) U2 (L' U R')} {(L U' R) U2 (L' U R')}"
                             " U")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "20.png\n"
                             "{(R' U L') U2 (R U' L)} {(R' U L') U2 (R U' L)}"
                             " U'")
        await message.answer("Next is '/eperm'")
    elif message.text.lower() == "/eperm":
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "03.png\n"
                             "x' (R U' R') D (R U R') u2 (R' U R) D (R' U' R)")
        await message.answer("Last and the biggest group is '/gperms'")
    elif message.text.lower() == "/gperms":
        await message.answer("This group is not only large but also hard. But "
                             "if you try you will succeed")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "15.png\n"
                             "R2 u R' U R' U' R u' R2 [y' R' U R]")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "16.png\n"
                             "[R' U' R] y R2 u R' U R U' R u' R2")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "14.png\n"
                             "R2 u' R U' R U R' u R2 [y R U' R']")
        await message.answer("https://ruwix.com/pics/fridrich/friedrich-pll-"
                             "17.png\n"
                             "[R U R'] y' R2 u' R U' R' U R' u R2")
        await message.answer("Lastly, I want to wish you that you achieve the "
                             "result you want!\n"
                             "Thank you for using my bot.")
