<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>wc as a service</title>
    <style>
        html,
        body {
            overflow: none;
            max-height: 100vh;
        }
    </style>
</head>

<body style="height: 100vh; text-align: center; background-color: black; color: white; display: flex; flex-direction: column; justify-content: center;">
    <?php
    if (!isset($_GET['file'])) {
        echo "shhhhs3cr3tstr1ng";
        header("Location: /?file=index.php");
        exit;
    }
    header("HTTP/1.0 302 Magic");

    ini_set('max_execution_time', 5);
        if ($_COOKIE['key'] != 'shhhhs3cr3tstr1ng') {
            setcookie('key', 'secret');
            die('Sorry, only people from csivit are allowed to access this page.');
        }
    ?>

    <h1>Character Count as a Service</h1>
    <form>
        <textarea style="border-radius: 1rem;" type="text" name="text" rows=30 cols=100></textarea><br />
        <input type="submit">
    </form>
    <?php
    if (isset($_GET["text"])) {
        $text = $_GET["text"];
        echo "<h2>The Character Count is: " . exec('printf \'' . $text . '\' | wc -c') . "</h2>";
    }
    ?>
</body>

</html>