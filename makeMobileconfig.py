import sys
import uuid
import base64
username = sys.argv[1]
email = sys.argv[2]
userCertificate_p12filename = sys.argv[3]
outputFilename = sys.argv[4]
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
			LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZZekNDQTB1
			Z0F3SUJBZ0lJUXBTRTFYbllUY0V3RFFZSktvWklodmNOQVFFRkJR
			QXdQekVMTUFrR0ExVUUKQmhNQ1EwZ3hFekFSQmdOVkJBb1RDbk4w
			Y205dVoxTjNZVzR4R3pBWkJnTlZCQU1URW5OMGNtOXVaMU4zWVc0
			ZwpVbTl2ZENCRFFUQWVGdzB4TkRFd01qa3hPREUzTkRKYUZ3MHlO
			REV3TWpZeE9ERTNOREphTUQ4eEN6QUpCZ05WCkJBWVRBa05JTVJN
			d0VRWURWUVFLRXdwemRISnZibWRUZDJGdU1Sc3dHUVlEVlFRREV4
			SnpkSEp2Ym1kVGQyRnUKSUZKdmIzUWdRMEV3Z2dJaU1BMEdDU3FH
			U0liM0RRRUJBUVVBQTRJQ0R3QXdnZ0lLQW9JQ0FRQzlSeFZZVGJq
			dwo1NkZ6VklRVWc3MXdLMGd3dmcxc1k3VkZmRDQyT1ZNSGphb0FE
			dkNMejVaZGZvSGJlZk91YTZ3R1dDVjVjSUFyCjVyaEZYM1JnS0dX
			cDdQenJ2b0xTcjllTW9vRkNxcmZjaDluNVI4cGlUQWpRalFTWjVC
			R2VSeVlTUGlXWGpMck0KbnFWaFFFS1JOZnJ4QVlMcWZnZ2VSZmky
			ZjFBaG1RUW1JUlZESGFiQUxSTTcxNVN6Q2pQeUpPMUc1M0MzeUlS
			RApvZ1VKOXI1dEFTbE9hSWJlbFNnaUgxU012NjF4MjJBK2FUUzRk
			UUFmTG5sVzNOV00yakpsRTRJdVlhbGxCSmRlCllsZmNCUjRPR0dS
			RDNaQ1k5N2xsQzIwV09jSUpWazRuMTB3dlNXcTU5dHFQODk2d1c2
			Z0xKV0JjbjMyTGxZQWoKcGFleCthZWtXdUJSV2lHV01nR2p3QnEz
			OEFQU216dmY2K1hqT2dacEFWRmx4bUhsQ2o2bmEyQnVwQjROMSsx
			WgpRdXhhaG1uL2phalpMUmRNQzBDdGVmOTlKZ1NRVTlJVHM3WVp6
			QjhmUVl1emRpdytkVXFtRGFUWTh1RlU5ZnA1CkZRTWd1LzlpS2Zj
			a0xlL1hFYmhXVkRrY3FtbmxNTGp2RkliK0xIcGFsZVFRYWRtTjJE
			WHE0QndBd1FJVmRsSHUKeXl2SXYvT1UxUjFEeU9YM1FBdmZLOWFF
			OGcvcW1UOVRRcFJURmtKZ29nNHl5dHFlYk1oNE5xZ1RmVHdrZ1VC
			dgphMlJjVFVFNG8vTGlVeUNXakc3VWZIaU1XWW9WUWFmbVZ4WTgz
			TTBZdjhuYjdabzJtd2Q0TEJ1YmVzQUMzaGt4CjlWQXFuQ3FFNWZZ
			MFBjMldQNExvbGU4TTB2WXRRMTZtNHdJREFRQUJvMk13WVRBUEJn
			TlZIUk1CQWY4RUJUQUQKQVFIL01BNEdBMVVkRHdFQi93UUVBd0lC
			QmpBZEJnTlZIUTRFRmdRVTVtaDlYTDl1TGtnUWMxaHh0cTdKQm9i
			dQphTFl3SHdZRFZSMGpCQmd3Rm9BVTVtaDlYTDl1TGtnUWMxaHh0
			cTdKQm9idWFMWXdEUVlKS29aSWh2Y05BUUVGCkJRQURnZ0lCQUVS
			eCtMbHh6VFdJZy9yc3hwTExxYTVWQ3pkQmZZTExDNy9KSFc5QzVV
			K3VzWXl5OUU1d1JOTjYKc09HRlVuSnhZd1RURVFRMzhHUnd4VkFH
			V0JLaG9EQ2xMRVg0MjBSbVBJZFZTZXRQRFVZeWVuclFOajNpQzRo
			Ygp4SFIvZ0NhbHVsSVFUbEk5bnNneEw4TzAyZENkL04xbTRPSnZ0
			SThSaVZoUjRpa0Vlb3Jvcm05MTZ0WTNkanp2Cm1rckJPVzRhNDBO
			dHh6TVBkZjRoTERSQzJ3T1hYYWhnR2RCaXhKYTlmektkRGdZVTFs
			VkFRd1E0TFFmNFZmOFAKdjhTMWVsY21ZendlbVczc3ZaRjNid21X
			SUhEbjVUd1Fjc204QnNCemhYQ2ZDZlpEbENZY2F6TG96M1lmRWZi
			Mwptb0xZb3U0OW1NRlF3UDNWZC9TckxoTUlYYlVZcmYyQ0IxM3Nm
			TFRhemtXK3BzK2YyVktBWmt3VWxuakNDU1NpCkpsemJzTGtWQktX
			YldqN052bXNQbHdIejF6ZE9oUW0wRlZJU0RxdmhGU1JNU3Z0VlE3
			b2xJRVJqNlJvY3ZMNWsKZHo4SU5MdkoxNE02VHljNGRrdWRva0pL
			ZmJ1Uy91bW1BVDFEZ2h6YXhXaHY3SEdFamVwSkQ0anBwZk9GaXdr
			Lwp3Mm1FcHJHUVc4eWpET1pIc2x2U3g5T2NQMEpRWERtUWdYcUNL
			TzJYMElsQ1J6ditGTzBtdzNTYmdOUVFkWjBGCkg3ZE1YZHp4K2JC
			V0o4dm1zOXNMQUVvR2VoYklLN09xZ1RoaFhlUy9qbjRsUXBPOTVu
			WmkwR0Zta0xZOVFHYWYKcjFHQWZpVnJYVit4NkRPMHNWUHJsQmJP
			TUdtSXRNSjQyMXRER0hwdWYwekNBOGpHME9OVQotLS0tLUVORCBD
			RVJUSUZJQ0FURS0tLS0tCg==
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
</plist>""".format(email, userCertificate_PayloadUUID, VPNSettings_PayloadIdentifier, VPNSettings_PayloadUUID, userCertificatePassword, userCertificate_p12filename, userCertificate, userCertificate_p12filename, userCertificate_payloadIdentifier, userCertificate_PayloadUUID, top_PayloadUUID)
out_fp.write(out)
