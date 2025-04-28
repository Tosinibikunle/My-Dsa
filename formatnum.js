function formatNumber(number, locale = 'en-US', options = {}) {
      return new Intl.NumberFormat(locale, options).format(number);
      }

      // Example:
      console.log(formatNumber(2500, 'en-US', { style: 'currency', currency: 'USD' }));
      // $2,500.00
