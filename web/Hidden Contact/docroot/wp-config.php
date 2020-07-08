<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'wordpress');

/** MySQL database password */
define('DB_PASSWORD', 'wordpress');

/** MySQL hostname */
define('DB_HOST', 'mysql');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '|`zk-!_yRw2_gpX%cV~,p{@Y+.Z5p|vV7xNK^al;cxI}tA3Zl(P<n9+YE-C-%C%[');
define('SECURE_AUTH_KEY',  '&w5Z/A-E37cS)VrrQaaM=7h9=fKUAYwD0h2AcMRL$H,xH><389 e@e C+a@rHGg_');
define('LOGGED_IN_KEY',    '!y!*hDRiok]d:6F- dvJN+E|ZSYaL1Eg%86lX!uB> i_`!qDoB-)CahiK)C$3J<v');
define('NONCE_KEY',        '(Tcl4p=;}{H/}GL]y!QARl]c:r=:^<2f@@yr8F0W-CQ,naG_ra455/+MhJT}O?LW');
define('AUTH_SALT',        'QuT~PS+$?Vp|1-G;qV$Ux~oi]B1v^;wtSr2|8<Dqm6A `OvJOpGmc|u|vL:z%%DD');
define('SECURE_AUTH_SALT', ' ;42d3yLc,7Vs2gZ4C~79o)x+|:Fl*8o2+[-Y+giJO@YO>~TP%n[x5!:(v`02>Jz');
define('LOGGED_IN_SALT',   '</Ne^c-+>RUjgQ+J0!~dya%H*|#+BAbeR]AU:Y|lx&C#~8*?Z9$.n>GngRpDzF=p');
define('NONCE_SALT',       'DGkm5!e4PKiryywv#?[Tm2$69F~+;&?of}IJ,C6$EL++f;H!8} L@8MpUzWX<(,2');


/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

// If we're behind a proxy server and using HTTPS, we need to alert Wordpress of that fact
// see also http://codex.wordpress.org/Administration_Over_SSL#Using_a_Reverse_Proxy
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') {
	$_SERVER['HTTPS'] = 'on';
}

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
