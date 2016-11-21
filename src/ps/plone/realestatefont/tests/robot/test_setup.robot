*** Settings ***

Resource  keywords.robot

Suite Setup  Setup
Suite Teardown  Teardown


*** Test cases ***

Show how to activate the add-on
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/prefs_install_products_form
    Page should contain element  xpath=//*[@value='ps.plone.realestatefont']
    Assign id to element
    ...  xpath=//*[@value='ps.plone.realestatefont']/ancestor::li
    ...  addons-psplonerealestatefont
    Assign id to element
    ...  xpath=//*[@value='ps.plone.realestatefont']/ancestor::ul/parent::*/parent::*
    ...  addons-enabled

    Highlight  addons-psplonerealestatefont
    Capture and crop page screenshot
    ...  setup_select_add_on.png
    ...  id=addons-enabled
