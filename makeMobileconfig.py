import sys
import uuid
import base64
username = sys.argv[1]
email = sys.argv[2]
userCertificate_p12filename = sys.argv[3]
strongswanCert_filename = sys.argv[4]
outputFilename = sys.argv[5]
out_fp = open(outputFilename, 'w')

userCertificate_fp = open(userCertificate_p12filename, 'r')
userCertificate_raw = userCertificate_fp.read()

userCertificate_PayloadUUID = uuid.uuid4()
VPNSettings_PayloadUUID = uuid.uuid4()
VPNSettings_PayloadIdentifier = "{}.com.apple.vpn.managed.{}".format(uuid.uuid4(),VPNSettings_PayloadUUID)
userCertificatePassword = username
usercertificateFilename = "{}.p12".format(username)
userCertificate = base64.b64encode(userCertificate_raw)
userCertificate_payloadIdentifier = "client.openvpn.net.{}.com.apple.security.pkcs12.{}".format(uuid.uuid4(),userCertificate_PayloadUUID)
top_PayloadUUID = uuid.uuid4()

strongswanCert_fp = open(strongswanCert_filename,'r')
strongswanCert_raw = strongswanCert_fp.read()
strongswanCert_base64 = base64.b64encode(strongswanCert_raw)



out="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>ConsentText</key>
	<dict>
		<key>default</key>
		<string>Take back your time </string>
	</dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>PayloadCertificateFileName</key>
			<string>strongswanCert.crt</string>
			<key>PayloadContent</key>
			<data>
			{}
			</data>
			<key>PayloadDescription</key>
			<string>Configures certificate settings.</string>
			<key>PayloadDisplayName</key>
			<string>strongSwan Root CA</string>
			<key>PayloadIdentifier</key>
			<string>client.openvpn.net.C054DFF0-5BDF-4896-8AAB-F27262D2AF8E.com.apple.security.root.49F08CBA-8551-4AF4-9054-E83B2F65780A</string>
			<key>PayloadType</key>
			<string>com.apple.security.root</string>
			<key>PayloadUUID</key>
			<string>49F08CBA-8551-4AF4-9054-E83B2F65780A</string>
			<key>PayloadVersion</key>
			<integer>1</integer>
		</dict>
		<dict>
			<key>IKEv2</key>
			<dict>
				<key>AuthenticationMethod</key>
				<string>Certificate</string>



<key>OnDemandEnabled</key>            
<integer>1</integer>
<key>OnDemandRules</key>
            
<array>
   <dict>
      <key>Action</key>
      <string>Disconnect</string>
      <key>SSIDMatch</key>
      <array>
         <string>My Home WiFi</string>
      </array>
   </dict>
   <dict>
      <key>Action</key>
      <string>EvaluateConnection</string>
      <key>ActionParameters</key>
      <array>
         <dict>
            <key>Domains</key>
               <array>
                  <string>*</string>
               </array>
            <key>RequiredURLStringProbe</key>
            <string>https://test-non-existent-URL-for-connectivity.com</string>
            <key>DomainAction</key>
            <string>ConnectIfNeeded</string>
         </dict>
      </array>
   </dict>
   <dict>
      <key>Action</key>
      <string>Connect</string>
   </dict>
</array>
            




                <key>ChildSecurityAssociationParameters</key>
				<dict>
					<key>DiffieHellmanGroup</key>
					<integer>2</integer>
					<key>EncryptionAlgorithm</key>
					<string>AES-256</string>
					<key>IntegrityAlgorithm</key>
					<string>SHA2-256</string>
					<key>LifeTimeInMinutes</key>
					<integer>1440</integer>
				</dict>
				<key>DeadPeerDetectionRate</key>
				<string>None</string>
				<key>ExtendedAuthEnabled</key>
				<false/>
				<key>IKESecurityAssociationParameters</key>
				<dict>
					<key>DiffieHellmanGroup</key>
					<integer>2</integer>
					<key>EncryptionAlgorithm</key>
					<string>AES-256</string>
					<key>IntegrityAlgorithm</key>
					<string>SHA2-256</string>
					<key>LifeTimeInMinutes</key>
					<integer>1440</integer>
				</dict>
				<key>LocalIdentifier</key>
                <string>{}</string>
				<key>PayloadCertificateUUID</key>
                <string>{}</string>
				<key>RemoteAddress</key>
				<string>strong.lesstechmorepeople.com</string>
				<key>RemoteIdentifier</key>
				<string>strong.lesstechmorepeople.com</string>
				<key>ServerCertificateCommonName</key>
				<string>strong.lesstechmorepeople.com</string>
				<key>ServerCertificateIssuerCommonName</key>
				<string>strongSwan Root CA</string>
			</dict>
			<key>IPv4</key>
			<dict>
				<key>OverridePrimary</key>
				<integer>1</integer>
			</dict>
			<key>PayloadDescription</key>
			<string>Configures VPN settings</string>
			<key>PayloadDisplayName</key>
			<string>VPN</string>
			<key>PayloadIdentifier</key>
            <string>{}</string>
			<key>PayloadType</key>
			<string>com.apple.vpn.managed</string>
			<key>PayloadUUID</key>
            <string>{}</string>
			<key>PayloadVersion</key>
			<real>1</real>
			<key>Proxies</key>
			<dict/>
			<key>UserDefinedName</key>
			<string>vpn_connection_name</string>
			<key>VPNType</key>
			<string>IKEv2</string>
		</dict>
		<dict>
			<key>Password</key>
            <string>{}</string>
			<key>PayloadCertificateFileName</key>
            <string>{}</string>
			<key>PayloadContent</key>
			<data>
                {}
            </data>
			<key>PayloadDescription</key>
			<string>Configures certificate settings.</string>
			<key>PayloadDisplayName</key>
            <string>{}</string>
			<key>PayloadIdentifier</key>
            <string>{}</string>
			<key>PayloadType</key>
			<string>com.apple.security.pkcs12</string>
			<key>PayloadUUID</key>
            <string>{}</string>
			<key>PayloadVersion</key>
			<integer>1</integer>
		</dict>
	</array>
	<key>PayloadDescription</key>
	<string>Settings to Cure internet over-use</string>
	<key>PayloadDisplayName</key>
	<string>Take Back Your Time</string>
	<key>PayloadIdentifier</key>
	<string>client.openvpn.net.C054DFF0-5BDF-4896-8AAB-F27262D2AF8E</string>
	<key>PayloadOrganization</key>
	<string>Matt Rosenthal</string>
	<key>PayloadRemovalDisallowed</key>
	<false/>
	<key>PayloadType</key>
	<string>Configuration</string>
	<key>PayloadUUID</key>
    <string>{}</string>
	<key>PayloadVersion</key>
	<integer>1</integer>
</dict>
</plist>""".format(strongswanCert_base64, email, userCertificate_PayloadUUID, VPNSettings_PayloadIdentifier, VPNSettings_PayloadUUID, userCertificatePassword, userCertificate_p12filename, userCertificate, userCertificate_p12filename, userCertificate_payloadIdentifier, userCertificate_PayloadUUID, top_PayloadUUID)
out_fp.write(out)
