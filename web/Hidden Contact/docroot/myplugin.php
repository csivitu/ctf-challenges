<?php
remove_action('wp_head', 'wp_generator');
// Hide wordpress version number
add_action('init', '_wp_noversion', 1);
function _wp_noversion()
{
    if (!is_admin()) {
        global $wp_version;
        $wp_version = '';
    }
}
