<?php

class MailChimpApi
{

    public function __construct()
    {
        add_action('wp_ajax_mcbSubmit_Form_Data', [$this, 'mcbSubmit_Form_Data']);
        add_action('wp_ajax_nopriv_mcbSubmit_Form_Data', [$this, 'mcbSubmit_Form_Data']);

        add_action('wp_ajax_mcbSubmit_Form_AudienceId', [$this, 'mcbSubmit_Form_AudienceId']);
        add_action('wp_ajax_nopriv_mcbSubmit_Form_AudienceId', [$this, 'mcbSubmit_Form_AudienceId']);
    }

    public function mcbSubmit_Form_Data()
    {

        if (!wp_verify_nonce(sanitize_text_field($_GET['nonce']), 'wp_rest')) {
            wp_die();
        }

        $apiKey = sanitize_text_field($_GET['apiKey']) ?? false;
        $audienceId = sanitize_text_field($_GET['audienceId']) ?? false;
        $email = sanitize_text_field($_GET['email']) ?? false;
        $fName = sanitize_text_field($_GET['fName']) ?? false;
        $lName = sanitize_text_field($_GET['lName']) ?? false;
        $dc = substr($apiKey, strpos($apiKey, '-') + 1);

        $mailDataCenterList = ["us1", "us2", "us3", "us4", "us5", "us6", "us7", "us8", "us9", "us10", "us11", "us12", "us13", "us14", "us15", "us16", "us17", "us18", "us19", "us20"];

        if (!in_array($dc, $mailDataCenterList)) {
            echo wp_json_encode(['success' => false, 'status' => 502, 'message' => 'Invalid API Key!']);
            wp_die();
        }

        if (!$audienceId) {
            echo wp_json_encode(['success' => false, 'status' => 510, 'message' => 'Audience ID Required!']);
            wp_die();
        }

        $response = wp_remote_post("https://$dc.api.mailchimp.com/3.0/lists/$audienceId/members", [
            "method" => "POST",
            "headers" => [
                "Authorization" => "apikey " . $apiKey,
                "Content-Type" => "application/json",
            ],
            "body" => wp_json_encode(
                [
                    "email_address" => $email,
                    "status" => "subscribed",
                    'merge_fields' => [
                        'FNAME' => $fName,
                        'LNAME' => $lName,
                    ],
                ]
            ),
        ]);

        echo wp_remote_retrieve_body($response);
        wp_die();

    }

    public function mcbSubmit_Form_AudienceId()
    {

        if (!wp_verify_nonce(sanitize_text_field($_GET['nonce']), 'wp_rest')) {
            wp_die();
        }

        $apiKey = sanitize_text_field($_GET['apiKey']) ?? false;
        $dc = substr($apiKey, strpos($apiKey, '-') + 1);

        $mailDataCenterList = ["us1", "us2", "us3", "us4", "us5", "us6", "us7", "us8", "us9", "us10", "us11", "us12", "us13", "us14", "us15", "us16", "us17", "us18", "us19", "us20"];

        if (!in_array($dc, $mailDataCenterList)) {
            echo wp_json_encode(['success' => false, 'status' => 502, 'message' => 'Invalid API Key!']);
            wp_die();
        }

        $res = wp_remote_get("https://$dc.api.mailchimp.com/3.0/lists?count=1000&offset=0", [
            "headers" => [
                "Authorization" => "Basic " . $apiKey,
                "Content-Type" => "application/json",
            ],
        ]);

        echo wp_send_json($res['body']);
    }
}
new MailChimpApi();
