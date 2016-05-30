### Adresses IP

Impression des adresses IP lorsqu'une interface est configurée.

`cat /etc/cron.d/print-ip`

    #
    # JMSinfo SAS
    #

    MAILTO=dev@jmsinfo.co

    @reboot root /opt/print-ip/print-ip.sh
