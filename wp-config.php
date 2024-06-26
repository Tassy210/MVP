	<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'Oieee_1234' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '&09p|`D`xZeQ2CynQ{gHgVldJR~ub#)(ma.O!X zryueYb|NY<>Q4O*&a0_.D:AH' );
define( 'SECURE_AUTH_KEY',  '!qy81q405<?Q>hY g#L?iqf7XcQdPw3QyJ>R^gCXmg(YM Pn#M?^r7Hh@w/l#S|]' );
define( 'LOGGED_IN_KEY',    'j,J$LOxwziNU,W?iTMsCy4;[~B+vR.MDn[P6M~Pjm#wAqSQZ2Y:1^FH;e=QGeR$s' );
define( 'NONCE_KEY',        '0jn&<#mnKBPh30*w=YW4+=]^>z<N4H/X2q--@d6u9aVaHJW,+/m#nzjLpENK$6%w' );
define( 'AUTH_SALT',        'C!dKFbn^<z!u~4i8RB|n3V8fucH@Rg!Mw)k_,Wzxy~kW@P-tv[qRkvNuNt_A]}I8' );
define( 'SECURE_AUTH_SALT', 'Jv`H/_uHzH|)nHac2,o]o8O2m*U:tlz,?P~@2gI5aDjLaK_mBaW1-qN:Mbj++8Vq' );
define( 'LOGGED_IN_SALT',   ',yCnMj}h!O}ibK.?HeC64q.a^%dJ7cOlV|-Y6^,e0PW.Vd.)11mS`.u8s!rSGlp`' );
define( 'NONCE_SALT',       'T^H5S`5-si]=L4}ADBY-VrVkR7lCmAcsNw]y<.>Psj}|4G &Z$Lo&/C^M^`W1*[s' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
