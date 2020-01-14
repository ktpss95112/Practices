<?php

# Useless changelog here
include_once('flag.php');
# TODO: Remove the source
# TODO: Remove useless comment
# TODO: Fire some people
# TODO: Remove useless TODO
# TODO: Rewrite the code
# TODO: Replace emoji to normal variable name
# TODO: Eat something
# TODO: Quit the job, maintain this is toooooo hard
show_source(__FILE__);
echo strlen($fllllllag) . "\n";
if ((isset($_POST['😂']) and isset($_POST['🤣']) and isset($_GET['KEY'])) or isset($_GET['is_this_flag？'])){
    srand(20191231 + 20200101 + time());
    $mystr = 'Happy';
    $mystr .= ' New';
    $mystr .= '  Year⁠!~~~';
    # Useless comment here
    $array1 = str_split($fllllllag, 1);
    # 2019-01-01
    # Alice: What is array1, array2, and array3 ????
    # 2019-12-31
    # Alice: Can someone explain to me?
    $array2 = str_split($mystr, 1);
    # Want to kill your colleague for shitty code?
    # Call 000000000 now
    $array3 = str_split($_GET['KEY'], 1);
    $final = '';
    # More useless changelog here
    foreach( $array1 as $value ){
    # 2019-12-31
    # Bob: This should be ok to protect our secret
    # Alice: No
    # Bob: Yes, it is
    # Alice: No!
    # Bob: prove it to me?
    # Ann: don't chat in here, plz
    # Bob: fine
        $final .= @strval(ord($value) ^ rand() ^ $array2[rand() % count($array2)] ^ ($array3[rand() % count($array3)] * random_int(1,128))) . ' ';
    }
    if ($_POST['​😂'] == md5($_POST['🤣​'])){
        # Remove this to gain some money for your job
        sleep(1);
        echo $final;
    }else{
        # Who did this shit?
        die('bye!');
    }

    # Our secret verify machine
    if ($fllllllag === $_GET['is_this_flag？']){
        echo 'Here is your flag haha: ' . $fllllllag;
    }
}else{
    # More random sleep for performance improve
    sleep(random_int(1,2));
    # Decided to quit your job?    
    die('bye!');
}
