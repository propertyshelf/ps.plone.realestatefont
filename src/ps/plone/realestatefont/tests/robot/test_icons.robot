*** Settings ***

Resource  keywords.robot

Suite Setup  Setup
Suite Teardown  Teardown


*** Test cases ***

Show the icon preview
    Go to  ${PLONE_URL}/psf-realestate-preview
    Page should contain element  id=font-preview

    Capture and crop page screenshot
    ...  preview_font.png
    ...  id=font-preview
