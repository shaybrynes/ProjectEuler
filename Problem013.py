"""
---*** THE PROBLEM ***---
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
.....

---*** SOLUTION NOTES ***---
To make this solution easier all 100 numbers were pack into one string. Then convert the list into the 100 50-digit
numbers the problem initiated with.
"""


def format_string(num_string, length):
    # 'num_string' is the string of numbers to be formatted, 'length' is the lengths that the string should be spliced
    # into.
    # Returns a list of all the numbers the string was cut into.

    list_numbers = []

    # Iterate over the whole string.
    for i in range(length, len(num_string) + 1, length):

        # Splice larger string into the smaller strings required for the problem.
        next_subpart = num_string[i - 50:i]

        # Cast the splice into intergers.
        list_numbers.append(int(next_subpart))

    return list_numbers


def sum_subparts(num_string, length):
    # 'num_string' is the string of numbers to be formatted, its parts will be summed.
    # Returns the sum of all the digits

    # Get a list of all the sub parts of the string.
    list_numbers = format_string(num_string, length)
    addition = 0

    # Iterate over all the list elements
    for i in range(0, len(list_numbers)):

        # Sum the elements together.
        addition += list_numbers[i]

    return addition


# Set program up for the initial conditions specified by the problem.
length = 50
number = "3710728753390210279879799822083759024651013574025046376937677490009712648124896970078050417018260538743249" \
         "8619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075" \
         "3934617117198031042104751377806324667689261670696623633820136378418383684178734361726757281128798128499794" \
         "0806548193159262169127588983273844274228917432520321923589422876796487670272189318474514457360013064390911" \
         "6721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231" \
         "9658675507932419333164906352462741904929101432445813822663347944758178925758677183372176619637515905792397" \
         "2824559883840758203565325359399008402633568948830189458628227828801811993848262820142781941399405675871511" \
         "7009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558" \
         "2971693888707715466499115593487603532921714970056938543700705768266846246214956500764717872944383776045328" \
         "2654108756828443191190634694037855217779295145361232725250002960710750825638156567108852583507214587657617" \
         "2410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683" \
         "0619328460811191061556940512689692519343254517283886419180470492932150586425630494836246722164843507620172" \
         "7918039944693004732956340691157324443869081257945140890577062294291971079282095503768752567877309186254074" \
         "4969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871" \
         "7201219257766954781828337579931036147403568564490955270978647975811672632010043689784255353992093183744149" \
         "7806860984484030981290777917990882187953273644756755908480308708698755139271185451707854416185242432069315" \
         "0332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541" \
         "0526847082990852113994273657341161827603150012716537860736150108085700914993951255702819874600437535829035" \
         "3174347173269321235781549826297425527373079495375976510530594696606768315657437716740187527588902802571733" \
         "2296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585" \
         "6299465806362379931407462559622407448690823117497779236546625724692332281091714191430288197103288597806669" \
         "7608929386382850253334033441306557801612781592181500556186883646842009047023053081172816430487623791969842" \
         "4872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225" \
         "5124867645336772018697169854431241957240991395900895231005882295548255300263520781532296796249481641953868" \
         "2187747608532713228572311042480345612486769706450799523637774242535411291684276865538926205024910326572967" \
         "2370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957" \
         "0145487928898485682772607771372140379887971538298203783031473527721580348144513491373226651381348295438291" \
         "9991818027891652243102739225112286953940957953066405232632538044100059654939159879593635297461521855023713" \
         "0764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771" \
         "0727504810239089552359745723189706772547915061505504953922979530901129967519861880882258753145295840992512" \
         "0382900940777077567211306739708304724483816533873502340845647058077308829591747671403631980081871290118754" \
         "9131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272" \
         "5125032755121603546981200581762165212827652751691296897789322381957343293399464375019078369457658833523998" \
         "8675506164965184775180738168837861091527357929701337621778427521926234019423996391680449839931733127313292" \
         "4185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080" \
         "0591547471830798392868535206946944540724768418225246744171615140364279822733480555562148189714261791034259" \
         "8647204516893989422179826088076852877836461827993463137677543078093633330189826420901084880252167467088321" \
         "5120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539" \
         "3808339651327408011116666278919814880877979418768761442300309844908514116066182629368283676474477923918033" \
         "5110989069790714857869440895529906536404474255760836599766457950966602439640990538960712019821997604759949" \
         "0197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231" \
         "5011948093772450487951509541009216458637547105984367917863916702118749243199570064191796977759902830069915" \
         "3687137119366149528113058763802784107544497330784078992311553556256114232242325503368544248891735344889911" \
         "5014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210" \
         "1467390585685579345814036278227032808261657077394832759223284594170652509451232523060822918802058777319719" \
         "8394501808880724296619808111977715854250201654509041324580978688277894872185961772107838435069186155435662" \
         "8840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591" \
         "789781264330331690"

# Find the sum of all the numbers of 'length' digits
solution = sum_subparts(number, length)

# Print the first 10 digits of the solution
print(str(solution)[0:10])
