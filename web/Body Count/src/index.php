<?php
if (isset($_GET['file'])) {
    require_once($_GET['file']);
} else {
    header('Location: /?file=wc.php');
}
