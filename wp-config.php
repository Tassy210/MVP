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
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress_2' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

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
define( 'AUTH_KEY',         '7;UcC`/)uX+-ZR(QOVqhrT;TtZ9+@@)q7Be`SgPan7-H%[;;E$:/_&>DVGp)51!n' );
define( 'SECURE_AUTH_KEY',  'o$^D.:BVoIXWQ3Qu}U!!ScTrLm#V/zITT &S@vJ.w+--j5v^q>S[` YD=:ab*A%2' );
define( 'LOGGED_IN_KEY',    '*mQo|zKF/DUa`;QTS36`U9`ky]`;Sn:Cqdaz_=UGoK7&vP$vxzl[RHgJ#B34;tx+' );
define( 'NONCE_KEY',        'e>}y(3~P`71hk?rM.0w/kfkvMI&jAW y$c:&m(B#RTMokL#IFFcjQ^jOf}oP$LvV' );
define( 'AUTH_SALT',        '$8OIfvw{PTWyrKeT*!To~Vco!|CWU^& 9hUt.lP6R5`K:[!cOsv$*Gdb^#Sp0A{A' );
define( 'SECURE_AUTH_SALT', ' 5NE62.:6weXDPzL4G[!{sc&av$8{T.b*1&zG2zIs<9{d47OHD /(~dDc4Oz($Zr' );
define( 'LOGGED_IN_SALT',   ';1=SzS:|e>j>y(}FxN8b~$IG4LBnT6qlp0~@qQ^I%;A,$5y] y+[`bLi-gC8%P6m' );
define( 'NONCE_SALT',       'Y^RfVsO;TrNdYVfi&4D~4*C_4J|k,te8oixR2GP,R59~_r~?o{W7;!L?hyCAX3G4' );

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
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
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
