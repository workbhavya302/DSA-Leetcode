class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails=set()
        
        for email in emails:
            # Split local and domain names by '@' boundary
            local, domain=email.split('@')
            
            # the '+' rule for ignoring everything after it
            local = local.split('+')[0]
            
            # the '.' rule for removing all periods
            local = local.replace('.', '')
            
            # Reconstruct and add to deduplication Set
            unique_emails.add(local + '@' + domain)
            
        return len(unique_emails)
