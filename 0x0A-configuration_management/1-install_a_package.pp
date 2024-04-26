#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package { 'werkzeug':
  ensure   => '2.0.2',  # Adjust as necessary for compatibility
  provider => 'pip3'
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
  require  => Package['werkzeug']
}
