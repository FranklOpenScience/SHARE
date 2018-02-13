from setuptools import setup, find_packages
from share import __version__

setup(
    name='share',
    version=__version__,
    packages=find_packages(exclude=('tests*')),
    provides=[
        'share.transformers',
        'share.harvesters'
    ],
    entry_points={
        'console_scripts': [
            'sharectl = share.bin.__main__:main',
        ],
        'share.transformers': [
            'ca.lwbin = share.transformers.ca_lwbin:LWBINTransformer',
            'com.biomedcentral = share.transformers.com_biomedcentral:BioMedCentralTransformer',
            'com.dailyssrn = share.transformers.com_dailyssrn:DailySSRNTransformer',
            'com.figshare = share.transformers.com_figshare:FigshareTransformer',
            'com.figshare.v2 = share.transformers.com_figshare_v2:FigshareV2Transformer',
            'com.mendeley.data = share.transformers.com_mendeley_data:MendeleyTransformer',
            'com.peerj = share.transformers.com_peerj:PeerJTransformer',
            'com.peerj.xml = share.transformers.com_peerj_xml:PeerJXMLTransformer',
            'com.researchregistry = share.transformers.com_researchregistry:RRTransformer',
            'com.springer = share.transformers.com_springer:SpringerTransformer',
            'edu.ageconsearch = share.transformers.edu_ageconsearch:AgeconTransformer',
            'edu.gwu = share.transformers.edu_gwu:GWScholarSpaceTransformer',
            'edu.harvarddataverse = share.transformers.edu_harvarddataverse:HarvardTransformer',
            'gov.clinicaltrials = share.transformers.gov_clinicaltrials:ClinicalTrialsTransformer',
            'gov.nih = share.transformers.gov_nih:NIHTransformer',
            'gov.nsfawards = share.transformers.gov_nsfawards:NSFTransformer',
            'gov.pubmedcentral.pmc = share.transformers.gov_pubmedcentral_pmc:PMCTransformer',
            'gov.scitech = share.transformers.gov_scitech:ScitechTransformer',
            'gov.usgs = share.transformers.gov_usgs:USGSTransformer',
            'io.osf = share.transformers.io_osf:OSFTransformer',
            'io.osf.preprints = share.transformers.io_osf_preprints:PreprintTransformer',
            'io.osf.registrations = share.transformers.io_osf_registrations:OSFRegistrationsTransformer',
            'mods = share.transformers.mods:MODSTransformer',
            'oai_dc = share.transformers.oai:OAITransformer',
            'org.arxiv = share.transformers.org_arxiv:ArxivTransformer',
            'org.biorxiv = share.transformers.org_biorxiv:BiorxivTransformer',
            'org.biorxiv.rss = share.transformers.org_biorxiv_rss:BiorxivRSSTransformer',
            'org.biorxiv.html = share.transformers.org_biorxiv_html:BiorxivHTMLTransformer',
            'org.crossref = share.transformers.org_crossref:CrossrefTransformer',
            'org.datacite = share.transformers.org_datacite:DataciteTransformer',
            'org.dataone = share.transformers.org_dataone:DataoneTransformer',
            'org.elife = share.transformers.org_elife:ElifeTransformer',
            'org.engrxiv = share.transformers.org_engrxiv:EngrxivTransformer',
            'org.ncar = share.transformers.org_ncar:NCARTransformer',
            'org.neurovault = share.transformers.org_neurovault:NeurovaultTransformer',
            'org.plos = share.transformers.org_plos:PLoSTransformer',
            'org.psyarxiv = share.transformers.org_psyarxiv:PsyarxivTransformer',
            'org.socialscienceregistry = share.transformers.org_socialscienceregistry:SCTransformer',
            'org.socarxiv = share.transformers.org_socarxiv:SocarxivTransformer',
            'org.swbiodiversity = share.transformers.org_swbiodiversity:SWTransformer',
            'v1_push = share.transformers.v1_push:V1Transformer',
        ],
        'share.harvesters': [
            'ca.lwbin = share.harvesters.ca_lwbin:LWBINHarvester',
            'com.biomedcentral = share.harvesters.com_biomedcentral:BiomedCentralHarvester',
            'com.figshare = share.harvesters.com_figshare:FigshareHarvester',
            'com.figshare.v2 = share.harvesters.com_figshare_v2:FigshareHarvester',
            'com.mendeley.data = share.harvesters.com_mendeley_data:MendeleyHarvester',
            'com.peerj = share.harvesters.com_peerj:PeerJHarvester',
            'com.researchregistry = share.harvesters.com_researchregistry:ResearchRegistryHarvester',
            'com.springer = share.harvesters.com_springer:SpringerHarvester',
            'edu.ageconsearch = share.harvesters.edu_ageconsearch:AgEconHarvester',
            'edu.gwu = share.harvesters.edu_gwu:GWScholarSpaceHarvester',
            'edu.harvarddataverse = share.harvesters.edu_harvarddataverse:HarvardDataverseHarvester',
            'gov.clinicaltrials = share.harvesters.gov_clinicaltrials:ClinicalTrialsHarvester',
            'gov.doepages = share.harvesters.gov_doepages:DoepagesHarvester',
            'gov.nih = share.harvesters.gov_nih:NIHHarvester',
            'gov.nsfawards = share.harvesters.gov_nsfawards:NSFAwardsHarvester',
            'gov.scitech = share.harvesters.gov_scitech:SciTechHarvester',
            'gov.usgs = share.harvesters.gov_usgs:USGSHarvester',
            'io.osf = share.harvesters.io_osf:OSFHarvester',
            'oai = share.harvesters.oai:OAIHarvester',
            'org.arxiv = share.harvesters.org_arxiv:ArxivHarvester',
            'org.biorxiv = share.harvesters.org_biorxiv:BiorxivHarvester',
            'org.biorxiv.rss = share.harvesters.org_biorxiv_rss:BiorxivHarvester',
            'org.biorxiv.html = share.harvesters.org_biorxiv_html:BiorxivHarvester',
            'org.crossref = share.harvesters.org_crossref:CrossRefHarvester',
            'org.dataone = share.harvesters.org_dataone:DataOneHarvester',
            'org.elife = share.harvesters.org_elife:ELifeHarvester',
            'org.ncar = share.harvesters.org_ncar:NCARHarvester',
            'org.neurovault = share.harvesters.org_neurovault:NeuroVaultHarvester',
            'org.plos = share.harvesters.org_plos:PLOSHarvester',
            'org.socialscienceregistry = share.harvesters.org_socialscienceregistry:SCHarvester',
            'org.swbiodiversity = share.harvesters.org_swbiodiversity:SWHarvester',
        ]
    }
)
