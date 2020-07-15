FROM php:7.4-apache

# Use the default production configuration
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
COPY . /var/www/html

RUN echo -e "csictf{1nj3ct10n_15_p41nfu1}\n$(cat /etc/passwd)" >> /etc/passwd

EXPOSE 80
