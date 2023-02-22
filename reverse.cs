using UnityEngine;
using UnityEngine.UI;
public class reverse : MonoBehaviour
{
    public Toggle toggle;
    public AK.Wwise.Event musicEvent;
    float maxDuration;
    float minDuration;
    public AK.Wwise.Event musicEventR;
    uint musicr;
    uint music;
    int mPosition;
    int mrPosition;
    int musicPosition;
    int musicrPosition;
    int max;
    void Start()
    {   
        toggle.onValueChanged.AddListener(OnToggleValueChanged);  
        
        AkUtilities.GetEventDurations(musicEvent.Id, ref maxDuration, ref minDuration);
      
        max = (int)(maxDuration*1000);
    }
    private void Update()
    {
        AkSoundEngine.GetSourcePlayPosition(music, out musicPosition);
        AkSoundEngine.GetSourcePlayPosition(musicr, out musicrPosition);
        mPosition = (max - musicrPosition);
        mrPosition = (max - musicPosition);
    }
    void OnToggleValueChanged(bool isOn)
    {
        if (isOn)
        {
            if (mPosition == max)
            {
                mPosition = 65000;
            }
            music = AkSoundEngine.PostEvent(musicEvent.Id, this.gameObject, 0x100000, MusicCallBack, null);
            AkSoundEngine.SeekOnEvent(musicEvent.Id, this.gameObject, mPosition, false);
        }
        else
        { 
            if (mrPosition == max)
            {
                mrPosition = 0;
            }
            musicr = AkSoundEngine.PostEvent(musicEventR.Id, this.gameObject, 0x100000, MusicCallBackR, null);
            AkSoundEngine.SeekOnEvent(musicEventR.Id, this.gameObject, mrPosition, false);
            
        }
    }

    void MusicCallBack(object in_cookie, AkCallbackType in_type, object in_info)
    {

    }
    void MusicCallBackR(object in_cookie, AkCallbackType in_type, object in_info)
    {
       
    }
}
