Get user order
^^^^^^^^^^^^^^

::
    GET /user/order/
    GET /user/order?display=[order_id1,order_id2,...,]

Response:

::
    Status: 400 ERROR
    {
        'version' : '1',
        'success' : 'true',
        'error' : {
               'code': 'xxx',
               'message': 'xxxx'
        },
        'order' : ''
    }
    
    Status: 200 OK
    {
        'version' : '1',
        'success' : 'true',
        'error' : {
               'code': '',
               'message': ''
        },
        'order' : {
            'id_customer' : 'customer id',
            'id_cart' : 'card id',
            'id_currency' : 'currency id',
            'current_state' : 'current state id', 
            'id_address_delivery' : 'address id',
            'id_address_invoice' : 'address id',
            'data_add' : 'date [yyyy-mm-dd hh:mm:ss]',
            'data_upd' : 'date [yyyy-mm-dd hh:mm:ss]',
            'payment' : 'Paypal, etc',
            'recyclable' : 'isBool',
            'gift' : 'isBool',
            'gift_message' : 'isMessage',
            'total_discounts' : 'isPrice',
            'total_discounts_tax_incl' : 'isPrice',
            'total_discounts_tax_excl' : 'isPrice',
            'total_paid' : 'isPrice',
            'total_paid_tax_incl' : 'isPrice',
            'total_paid_tax_excl' : 'isPrice',
            'total_paid_real' : 'isPrice',
            'total_products' : 'isPrice',
            'total_products_wt' : 'isPrice',
            'total_shipping' : 'isPrice',
            'total_shipping_tax_incl' : 'isPrice',
            'total_shipping_tax_excl' : 'isPrice',
            'carrier_tax_rate' : 'isFloat',
            'total_wrapping' : 'isPrice',
            'total_wrapping_tax_incl' : 'isPrice',
            'total_wrapping_tax_excl' : 'isPrice',
            'shipping_number' : 'isTrackingNumber',
            'conversion_rate' : 'isFloat',
            'associations' : {
                'order_rows' : {
                    'order_row' : {
                        'product_id' : 'int',
                        'product_attr_id' : 'int',
                        'product_quantity' : 'int',
                        'product_name' : 'string',
                        'product_reference' : 'string',
                        'product_price' : 'isPrice',
                        'unit_price_tax_incl' : 'isPrice',
                        'unit_price_tax_excl' : 'isPrice',
                    }
                }
            }
        }
    }
